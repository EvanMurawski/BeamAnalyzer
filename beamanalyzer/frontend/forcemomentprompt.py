# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './beamanalyzer/frontend/forcemomentprompt.ui'
#
# Created: Sun Aug  3 21:06:54 2014
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

class Ui_Force_Moment_Dialog(object):
    def setupUi(self, Force_Moment_Dialog):
        Force_Moment_Dialog.setObjectName(_fromUtf8("Force_Moment_Dialog"))
        Force_Moment_Dialog.resize(400, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Force_Moment_Dialog.sizePolicy().hasHeightForWidth())
        Force_Moment_Dialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtGui.QDialogButtonBox(Force_Moment_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Force_Moment_Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 70, 371, 27))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.widget1 = QtGui.QWidget(Force_Moment_Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 50, 271, 17))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_location = QtGui.QLabel(self.widget1)
        self.label_location.setObjectName(_fromUtf8("label_location"))
        self.horizontalLayout_2.addWidget(self.label_location)
        self.label_magnitude = QtGui.QLabel(self.widget1)
        self.label_magnitude.setObjectName(_fromUtf8("label_magnitude"))
        self.horizontalLayout_2.addWidget(self.label_magnitude)

        self.retranslateUi(Force_Moment_Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Force_Moment_Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Force_Moment_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Force_Moment_Dialog)

    def retranslateUi(self, Force_Moment_Dialog):
        Force_Moment_Dialog.setWindowTitle(_translate("Force_Moment_Dialog", "Force Prompt", None))
        self.checkBox.setText(_translate("Force_Moment_Dialog", "Unknown?", None))
        self.label_location.setText(_translate("Force_Moment_Dialog", "Location:", None))
        self.label_magnitude.setText(_translate("Force_Moment_Dialog", "Magnitude:", None))

