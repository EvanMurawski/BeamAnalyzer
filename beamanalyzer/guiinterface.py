"""A GUI, implemented with PyQt4

BeamAnalyzer v0.3.0
Copyright 2014 Evan Murawski
License: MIT
"""

__about = 'BeamAnalyzer v0.3.0\n\nCopyright 2014 Evan Murawski\nLicense: MIT'
__version = 'v0.3.0'

from PyQt4 import QtCore, QtGui
from frontend.guistructure import Ui_Beam
from frontend.forcemomentprompt import Ui_Force_Moment_Dialog
from frontend.distforceprompt import Ui_Dist_Force_Dialog
from backend.interactions import Force, Interaction, InteractionLocationError, Moment, Dist_Force
from backend.beam import Beam
import backend.solver as solver
from backend.solver import SolverError
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt
import backend.shearmomentgenerator as shearmomentgenerator
from backend.shearmomentgenerator import Shear_Moment_Error 
import numpy as np
from frontend.mainwindow import Ui_MainWindow
from frontend.settingsdialog import Ui_Dialog_settings
import sys


def update_tree(beam):
    """Updates the tree widget based on the beam it is passed."""

    ui.treeWidget.clear()
    for item in beam.interactions:
        ui.treeWidget.addTopLevelItem(QtGui.QTreeWidgetItem(item.to_list()))


def unknown_state_change(lineEdit, label, ui, ok):
    """swaps the visibililty of the lineEdit and label. Updates the ok button state."""

    lineEdit.setVisible(not lineEdit.isVisible())
    label.setVisible(not label.isVisible())
    adjust_ok_buttons_state(ui, ok)


def force_moment_dialog_input_acceptable(ui):
    """Checks if the force moment dialog input is acceptable"""

    if ui.lineEdit_2.isVisible():
        return ui.lineEdit.hasAcceptableInput() and ui.lineEdit_2.hasAcceptableInput()
    else:
        return ui.lineEdit.hasAcceptableInput()


def adjust_ok_buttons_state(ui, ok):
    """Adjusts the state of the ok buttons for the force moment dialog"""

    if force_moment_dialog_input_acceptable(ui):
        ok.setEnabled(True)
    else:
        ok.setEnabled(False)


def dist_force_dialog_input_acceptable(ui):
    """Checks if the input is acceptable in the dist force dialog."""

    return (ui.lineEdit_start.hasAcceptableInput() and ui.lineEdit_end.hasAcceptableInput() and 
            ui.lineEdit_magnitude.hasAcceptableInput())


def adjust_ok_buttons_state_dist(ui, ok, end_validator):
    """Adjust the state of the ok buttons for teh dist force dialog"""

    if dist_force_dialog_input_acceptable(ui):
        ok.setEnabled(True)
    else:
        ok.setEnabled(False)

    end_validator.setRange(float(ui.lineEdit_start.text()) if ui.lineEdit_start.text() else beam.length, beam.length, 5)


def interaction_prompt(is_force):
    """Create an force moment dialog if is_force, else a moment dialog."""
 
    #Create the dialog
    dialog = QtGui.QDialog()
    dialog_ui = Ui_Force_Moment_Dialog()
    dialog_ui.setupUi(dialog)

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
    dialog_ui.checkBox.stateChanged.connect(lambda: unknown_state_change(dialog_ui.lineEdit_2, 
                                            dialog_ui.label_magnitude, dialog_ui, ok))

    #Initially, cursor in first line edit box
    dialog_ui.lineEdit.setFocus()

    #Show the dialog
    dialog.exec_()

    #If ok is pressed, create the new force / moment
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

        #Add the interaction to the beam.
        beam.add_interaction(interaction)

        update_tree(beam)


def add_force_clicked():
    """If the add force button is clicked, display the prompt"""

    interaction_prompt(True)


def add_moment_clicked():
    """If the add moment button is clicked, display the prompt"""

    interaction_prompt(False)


def add_distforce_clicked():

    #Create the dialog
    dialog = QtGui.QDialog()
    dialog_ui = Ui_Dist_Force_Dialog()
    dialog_ui.setupUi(dialog)
         
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

    #If ok is pressed, create the new distributed force
    if dialog.result():

        interaction = Dist_Force(float(dialog_ui.lineEdit_start.text()), float(dialog_ui.lineEdit_magnitude.text()), 
                                 float(dialog_ui.lineEdit_end.text()))

        beam.add_interaction(interaction)

        update_tree(beam)


def solve_clicked():
    """Solve is clicked - solve the beam and update the tree."""

    try:
        solver.solve(beam)
    except SolverError as e:
        QtGui.QMessageBox.warning(window,"Error", str(e))
        return

    update_tree(beam)

def plot_clicked():
    """Generate and display the force moment plot."""

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

    #apply a buffer around the plot for easier viewing
    shear_plot.axis([min(x), max(x), min(shear) - plot_margin * (max(shear)-min(shear)), max(shear) + 
                        plot_margin * (max(shear)-min(shear))])

    moment_plot.axis([min(x), max(x), min(moment) - plot_margin * (max(moment)-min(moment)), max(moment) + 
                        plot_margin * (max(moment)-min(moment))])

    #update the canvas
    canvas.draw()

def clear_clicked():
    """Clear the beam of all interactions. Update the tree and clear the force moment plot."""

    global beam
    beam = Beam(beam.length)
    update_tree(beam)
    plt.clf()
    canvas.draw()


def new_clicked():
    """Prompt for a new beam length. If input is ok, clear the beam, tree, and plot. 
    Create a new beam of the given length."""

    global beam
    length, ok = QtGui.QInputDialog.getDouble(window, "Beam Length",
            "Enter the length of the beam:", 0, 0, sys.float_info.max, 5)
    if ok:
        beam = Beam(length)
        update_tree(beam)
        plt.clf()
        canvas.draw()


def quit_clicked():
    """Quit the application."""

    app.quit()

def settings_clicked():
    """Create a settings dialog, containing the option to change the step size.
    If a valid new step size is entered, update the step size."""

    global step_size

    #Create the dialog
    dialog = QtGui.QDialog()
    dialog_ui = Ui_Dialog_settings()
    dialog_ui.setupUi(dialog)

    #Populate the line edit
    dialog_ui.lineEdit_step.setText(str(step_size))

    #set up the validator and apply it
    step_validator = QtGui.QDoubleValidator()
    step_validator.setRange(0.000001, 1000, 6)
    dialog_ui.lineEdit_step.setValidator(step_validator)

    dialog.exec_()

    #Update the step size if necessary
    if dialog.result():
        if dialog_ui.lineEdit_step.text() and float(dialog_ui.lineEdit_step.text()) != 0:
            step_size = float(dialog_ui.lineEdit_step.text())


def about_clicked():
    """Show the about dialog."""

    QtGui.QMessageBox.about(window, "About BeamAnalyzer", __about)


def clear_selected_clicked():
    """Clear the selected item, update the tree and clear the plot if something was removed."""

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
    """Make the first beam. This is required. If it is not done, exit the app."""

    ok = False
    length, ok = QtGui.QInputDialog.getDouble(window, "Beam Length",
        "Enter the length of the beam:", 0, 0, sys.float_info.max, 5)

    if ok:
        return Beam(length)
    else:
        sys.exit()


def make_links():
    """Establish the links between various actions and their corresponding functions."""

    ui.pushButton_force.clicked.connect(add_force_clicked)
    ui.pushButton_moment.clicked.connect(add_moment_clicked)
    ui.pushButton_distforce.clicked.connect(add_distforce_clicked)
    ui.pushButton_solve.clicked.connect(solve_clicked)
    ui.pushButton_plot.clicked.connect(plot_clicked)
    ui.pushButton_clear.clicked.connect(clear_clicked)
    ui.pushButton_new.clicked.connect(new_clicked)
    ui.pushButton_clearselected.clicked.connect(clear_selected_clicked)
    main_window_ui.actionQuit.triggered.connect(quit_clicked)
    main_window_ui.actionAbout.triggered.connect(about_clicked)
    main_window_ui.actionSettings.triggered.connect(settings_clicked)


if __name__ == '__main__':

    #Global vars
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

    #Show the window, maximized
    main_window.showMaximized()

    #setup links
    make_links()

    #setup beam
    beam = make_first_beam()

    #Exit shell when window exits
    sys.exit(app.exec_())