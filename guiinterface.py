from PyQt4 import QtCore, QtGui
from guistructure import Ui_Beam
from forcemomentprompt import Ui_Force_Moment_Dialog
from distforceprompt import Ui_Dist_Force_Dialog
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
from mainwindow import Ui_MainWindow
import sys


def update_tree(beam):
    ui.treeWidget.clear()
    
    for item in beam.interactions:
        ui.treeWidget.addTopLevelItem(QtGui.QTreeWidgetItem(item.to_list()))


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

def dist_force_dialog_input_acceptable(ui):
    return ui.lineEdit_start.hasAcceptableInput() and ui.lineEdit_end.hasAcceptableInput() and ui.lineEdit_magnitude.hasAcceptableInput()

def adjust_ok_buttons_state_dist(ui, ok, end_validator):
    if dist_force_dialog_input_acceptable(ui):
        ok.setEnabled(True)
    else:
        ok.setEnabled(False)

    end_validator.setRange(float(ui.lineEdit_start.text()) if ui.lineEdit_start.text() else beam.length, beam.length, 5)

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

    dialog_ui.lineEdit.setFocus()

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

    #Create the dialog
    dialog = QtGui.QDialog()
    dialog_ui = Ui_Dist_Force_Dialog()
    dialog_ui.setupUi(dialog)

    #Setup stuff
         
    #Initially, hide the ok button
    ok = dialog_ui.buttonBox.button(QtGui.QDialogButtonBox.Ok)
    ok.setEnabled(False)

    #Setup input validators
    start_validator = QtGui.QDoubleValidator()
    start_validator.setRange(0, beam.length, 5)

    end_validator = QtGui.QDoubleValidator()
    end_validator.setRange(0, beam.length, 5)

    magnitude_validator = QtGui.QDoubleValidator()
    magnitude_validator.setDecimals(5)

    #Apply the input validators
    dialog_ui.lineEdit_start.setValidator(start_validator)
    dialog_ui.lineEdit_end.setValidator(end_validator)
    dialog_ui.lineEdit_magnitude.setValidator(magnitude_validator)

    #Adjust the visibility of the ok button if the input is changed
    dialog_ui.lineEdit_start.textChanged.connect(lambda: adjust_ok_buttons_state_dist(dialog_ui, ok, end_validator))
    dialog_ui.lineEdit_end.textChanged.connect(lambda: adjust_ok_buttons_state_dist(dialog_ui, ok, end_validator))
    dialog_ui.lineEdit_magnitude.textChanged.connect(lambda: adjust_ok_buttons_state_dist(dialog_ui, ok, end_validator))

    #Set the focus
    dialog_ui.lineEdit_start.setFocus()

    #Show the dialog
    dialog.exec_()

    #If ok is pressed, create the new force
    if dialog.result():

        interaction = Dist_Force(float(dialog_ui.lineEdit_start.text()), float(dialog_ui.lineEdit_magnitude.text()), float(dialog_ui.lineEdit_end.text()))

        beam.add_interaction(interaction)

        update_tree(beam)

        print(beam)


def solve_clicked():
    try:
        solver.solve(beam)
    except SolverError as e:
        QtGui.QMessageBox.warning(window,"Error", str(e))
        return

    update_tree(beam)

def plot_clicked():

    if len(beam.interactions) < 1:
        QtGui.QMessageBox.warning(window,"Error", "There is nothing to plot.")
        return

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

def new_clicked():

    global beam

    length, ok = QtGui.QInputDialog.getDouble(window, "Beam Length",
            "Enter the length of the beam:", 0, 0, sys.float_info.max, 5)
    if ok:
        beam = Beam(length)
        update_tree(beam)
        plt.clf()
        canvas.draw()

def quit_clicked():
    app.quit()

def settings_clicked():
    pass

def show_menu():
    pass

def clear_selected_clicked():
    items = ui.treeWidget.selectedItems()
    
    removed = False

    for item in items:
        index = ui.treeWidget.indexOfTopLevelItem(item)
        if index != -1:
            removed = True
            beam.interactions.pop(index)

    if removed:
        update_tree(beam)
        plt.clf()
        canvas.draw()

def make_first_beam():

    ok = False

    while not ok:
        length, ok = QtGui.QInputDialog.getDouble(window, "Beam Length",
            "Enter the length of the beam:", 0, 0, sys.float_info.max, 5)

    return Beam(length)


def make_links():
    ui.pushButton_force.clicked.connect(add_force_clicked)
    ui.pushButton_moment.clicked.connect(add_moment_clicked)
    ui.pushButton_distforce.clicked.connect(add_distforce_clicked)
    ui.pushButton_solve.clicked.connect(solve_clicked)
    ui.pushButton_plot.clicked.connect(plot_clicked)
    ui.pushButton_clear.clicked.connect(clear_clicked)
    ui.pushButton_new.clicked.connect(new_clicked)
    ui.pushButton_clearselected.clicked.connect(clear_selected_clicked)
    main_window_ui.actionQuit.triggered.connect(quit_clicked)
    main_window_ui.actionSettings.triggered.connect(settings_clicked)
    ui.treeWidget.customContextMenuRequested.connect(show_menu)

if __name__ == '__main__':

    #Other Global Vars
    step_size = 0.01
    plot_margin = 0.15

    #Setup UI window
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    ui = Ui_Beam()
    ui.setupUi(window)

    #Setup main window
    main_window = QtGui.QMainWindow()
    main_window_ui = Ui_MainWindow()
    main_window_ui.setupUi(main_window)

    main_window.setCentralWidget(window)

    #setup matplotlib
    figure = plt.figure()
    canvas = FigureCanvas(figure)
    toolbar = NavigationToolbar(canvas, window)
    ui.verticalLayout_3.addWidget(toolbar)
    ui.verticalLayout_3.addWidget(canvas)

    #setup context menu
    ui.treeWidget.setContextMenuPolicy(3)


    #Show the window
    main_window.show()

    #setup links
    make_links()

    #setup beam
    beam = make_first_beam()

    #Exit shell when window exits
    sys.exit(app.exec_())


