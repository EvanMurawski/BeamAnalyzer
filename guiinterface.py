from PyQt4 import QtCore, QtGui
from guistructure import Ui_Beam
from beam import Beam
import sys


def add_force_clicked():
    print("addforce")

def add_moment_clicked():
    pass

def add_distforce_clicked():
    pass

def solve_clicked():
    pass

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