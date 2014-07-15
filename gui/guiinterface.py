from PyQt4 import QtCore, QtGui
from qttest import Ui_Beam_GUI
import sys


if __name__ == '__main__':

    #Setup UI
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Beam_GUI)
    ui.setupUi(window)
    window.show()

    



    sys.exit(app.exec_())