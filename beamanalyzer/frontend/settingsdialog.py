# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './beamanalyzer/frontend/settingsdialog.ui'
#
# Created: Sun Aug  3 18:24:05 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_settings(object):
    def setupUi(self, Dialog_settings):
        Dialog_settings.setObjectName(_fromUtf8("Dialog_settings"))
        Dialog_settings.resize(400, 250)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_settings)
        self.buttonBox.setGeometry(QtCore.QRect(30, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Dialog_settings)
        self.widget.setGeometry(QtCore.QRect(30, 50, 199, 56))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_step = QtGui.QLineEdit(self.widget)
        self.lineEdit_step.setObjectName(_fromUtf8("lineEdit_step"))
        self.horizontalLayout.addWidget(self.lineEdit_step)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_settings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_settings)

    def retranslateUi(self, Dialog_settings):
        Dialog_settings.setWindowTitle(_translate("Dialog_settings", "Settings", None))
        self.label_2.setText(_translate("Dialog_settings", "Solver:", None))
        self.label.setText(_translate("Dialog_settings", "Step Size:", None))

