from PyQt4 import QtCore, QtGui
from guistructure import Ui_Beam
from forcemomentprompt import Ui_Force_Moment_Dialog
from interactions import Force, Interaction, InteractionLocationError, Moment, Dist_Force
from beam import Beam
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

def add_force_clicked():

    #Create the dialog
    dialog = QtGui.QDialog()
    dialog_ui = Ui_Force_Moment_Dialog()
    dialog_ui.setupUi(dialog)

    #Setup stuff

        
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
        if dialog_ui.checkBox.checkState():
            force = Force(float(dialog_ui.lineEdit.text()), 0, False)
        else:
            force = Force(float(dialog_ui.lineEdit.text()), float(dialog_ui.lineEdit_2.text()))

        beam.add_interaction(force)

        update_tree(beam)


def add_moment_clicked():
    pass

def add_distforce_clicked():
    pass

def solve_clicked():
    print(beam)

def plot_clicked():
    pass


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


if __name__ == '__main__':


    #Setup UI window
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    ui = Ui_Beam()
    ui.setupUi(window)
    window.show()

    #setup links
    make_links()

    #setup beam
    beam = Beam(get_length())


    #Exit shell when window exits
    sys.exit(app.exec_())