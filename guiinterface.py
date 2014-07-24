from PyQt4 import QtCore, QtGui
from guistructure import Ui_Beam
from forcemomentprompt import Ui_Force_Moment_Dialog
from interactions import Force, Interaction, InteractionLocationError, Moment, Dist_Force
from beam import Beam
import solver
from solver import SolverError
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt
import shearmomentgenerator
from shearmomentgenerator import Shear_Moment_Error 
import numpy as np
import sys
#TODO: make a function in interaction that returns a list of strings representing the interaction



def update_tree(beam):
    ui.treeWidget.clear()
    
    for item in beam.interactions:
        ui.treeWidget.addTopLevelItem(QtGui.QTreeWidgetItem([item.__class__.__name__, 
                                                                str(item.location) + " , "+ str(item.end) if isinstance(item, Dist_Force) else str(item.location), 
                                                                str(item.magnitude) if item.known else 'N/A', 
                                                                "Known" if item.known else "Unknown"]))


def unknown_state_change(lineEdit, label, ui, ok):
    lineEdit.setVisible(not lineEdit.isVisible())
    label.setVisible(not label.isVisible())
    adjust_ok_buttons_state(ui, ok)

def force_moment_dialog_input_acceptable(ui):
    if ui.lineEdit_2.isVisible():
        return ui.lineEdit.hasAcceptableInput() and ui.lineEdit_2.hasAcceptableInput()
    else:
        return ui.lineEdit.hasAcceptableInput()

def adjust_ok_buttons_state(ui, ok):
    if force_moment_dialog_input_acceptable(ui):
        ok.setEnabled(True)
    else:
        ok.setEnabled(False)

def interaction_prompt(is_force):
 
    #Create the dialog
    dialog = QtGui.QDialog()
    dialog_ui = Ui_Force_Moment_Dialog()
    dialog_ui.setupUi(dialog)

    #Setup stuff

    #Set the name
    if is_force:
        dialog.setWindowTitle("New Force")
    else:
        dialog.setWindowTitle("New Moment")
         
    #Initially, hide the ok button
    ok = dialog_ui.buttonBox.button(QtGui.QDialogButtonBox.Ok)
    ok.setEnabled(False)

    #Setup input validators
    location_validator = QtGui.QDoubleValidator()
    location_validator.setRange(0, beam.length, 5)

    magnitude_validator = QtGui.QDoubleValidator()
    magnitude_validator.setDecimals(5)

    #Apply the input validators
    dialog_ui.lineEdit.setValidator(location_validator)
    dialog_ui.lineEdit_2.setValidator(magnitude_validator)

    #Adjust the visibility of the ok button if the input is changed
    dialog_ui.lineEdit.textChanged.connect(lambda: adjust_ok_buttons_state(dialog_ui, ok))
    dialog_ui.lineEdit_2.textChanged.connect(lambda: adjust_ok_buttons_state(dialog_ui, ok))

    #Update the visibility of the input boxes if the checkbox state is changed
    dialog_ui.checkBox.stateChanged.connect(lambda: unknown_state_change(dialog_ui.lineEdit_2, dialog_ui.label_magnitude, dialog_ui, ok))

    #Show the dialog
    dialog.exec_()

    #If ok is pressed, create the new force
    if dialog.result():
        if is_force:
            if dialog_ui.checkBox.checkState():
                interaction = Force(float(dialog_ui.lineEdit.text()), 0, False)
            else:
                interaction = Force(float(dialog_ui.lineEdit.text()), float(dialog_ui.lineEdit_2.text()))
        else:
            if dialog_ui.checkBox.checkState():
                interaction = Moment(float(dialog_ui.lineEdit.text()), 0, False)
            else:
                interaction = Moment(float(dialog_ui.lineEdit.text()), float(dialog_ui.lineEdit_2.text()))

        beam.add_interaction(interaction)

        update_tree(beam)

def add_force_clicked():
    interaction_prompt(True)


def add_moment_clicked():
    interaction_prompt(False)

def add_distforce_clicked():
    pass

def solve_clicked():
    try:
        solver.solve(beam)
    except SolverError as e:
        QtGui.QMessageBox.warning(window,"Error", str(e))
        return

    update_tree(beam)

def plot_clicked():

    #Clear the plot
    plt.clf()

    #Generate the shear and moment points, using generate_numerical
    try:
        shear_moment = shearmomentgenerator.generate_numerical(beam, step_size)
    except Shear_Moment_Error as e:
        QtGui.QMessageBox.warning(window,"Error", str(e))
        return
    
    #Plot the points
    x = np.arange(0, beam.length, step_size)

    shear = [y[0] for y in shear_moment]
    moment = [y[1] for y in shear_moment]

    shear_plot = figure.add_subplot(211)
    shear_plot.plot(x, shear)
    plt.title('Shear')

    moment_plot = figure.add_subplot(212)
    moment_plot.plot(x, moment)
    plt.title('Moment')

    shear_plot.axis([min(x), max(x), min(shear) - plot_margin * (max(shear)-min(shear)), max(shear) + plot_margin * (max(shear)-min(shear))])
    moment_plot.axis([min(x), max(x), min(moment) - plot_margin * (max(moment)-min(moment)), max(moment) + plot_margin * (max(moment)-min(moment))])

    #update the canvas
    canvas.draw()

def clear_clicked():
    global beam
    beam = Beam(beam.length)
    update_tree(beam)
    plt.clf()
    canvas.draw()

def get_length():

    length, ok = QtGui.QInputDialog.getDouble(window, "Beam Length",
        "Enter the length of the beam:", 0, 0, sys.float_info.max, 5)

    return length


def make_links():
    ui.pushButton_force.clicked.connect(add_force_clicked)
    ui.pushButton_moment.clicked.connect(add_moment_clicked)
    ui.pushButton_distforce.clicked.connect(add_distforce_clicked)
    ui.pushButton_solve.clicked.connect(solve_clicked)
    ui.pushButton_plot.clicked.connect(plot_clicked)
    ui.pushButton_clear.clicked.connect(clear_clicked)


if __name__ == '__main__':

    #Other Global Vars
    step_size = 0.01
    plot_margin = 0.15

    #Setup UI window
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    ui = Ui_Beam()
    ui.setupUi(window)
    

    #setup matplotlib
    figure = plt.figure()
    canvas = FigureCanvas(figure)
    toolbar = NavigationToolbar(canvas, window)
    ui.verticalLayout_3.addWidget(toolbar)
    ui.verticalLayout_3.addWidget(canvas)

    #Show the window
    window.show()

    #setup links
    make_links()

    #setup beam
    beam = Beam(get_length())


    #Exit shell when window exits
    sys.exit(app.exec_())