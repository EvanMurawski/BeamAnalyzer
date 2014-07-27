# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distforceprompt.ui'
#
# Created: Sun Jul 27 17:10:11 2014
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

class Ui_Dist_Force_Dialog(object):
    def setupUi(self, Dist_Force_Dialog):
        Dist_Force_Dialog.setObjectName(_fromUtf8("Dist_Force_Dialog"))
        Dist_Force_Dialog.resize(425, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dist_Force_Dialog.sizePolicy().hasHeightForWidth())
        Dist_Force_Dialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtGui.QDialogButtonBox(Dist_Force_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dist_Force_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 401, 27))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_start = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_start.sizePolicy().hasHeightForWidth())
        self.lineEdit_start.setSizePolicy(sizePolicy)
        self.lineEdit_start.setObjectName(_fromUtf8("lineEdit_start"))
        self.horizontalLayout.addWidget(self.lineEdit_start)
        self.lineEdit_end = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_end.sizePolicy().hasHeightForWidth())
        self.lineEdit_end.setSizePolicy(sizePolicy)
        self.lineEdit_end.setObjectName(_fromUtf8("lineEdit_end"))
        self.horizontalLayout.addWidget(self.lineEdit_end)
        self.lineEdit_magnitude = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_magnitude.sizePolicy().hasHeightForWidth())
        self.lineEdit_magnitude.setSizePolicy(sizePolicy)
        self.lineEdit_magnitude.setObjectName(_fromUtf8("lineEdit_magnitude"))
        self.horizontalLayout.addWidget(self.lineEdit_magnitude)
        self.layoutWidget1 = QtGui.QWidget(Dist_Force_Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 401, 17))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_location = QtGui.QLabel(self.layoutWidget1)
        self.label_location.setObjectName(_fromUtf8("label_location"))
        self.horizontalLayout_2.addWidget(self.label_location)
        self.label_magnitude = QtGui.QLabel(self.layoutWidget1)
        self.label_magnitude.setObjectName(_fromUtf8("label_magnitude"))
        self.horizontalLayout_2.addWidget(self.label_magnitude)
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)

        self.retranslateUi(Dist_Force_Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dist_Force_Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dist_Force_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dist_Force_Dialog)

    def retranslateUi(self, Dist_Force_Dialog):
        Dist_Force_Dialog.setWindowTitle(_translate("Dist_Force_Dialog", "New Distributed Force", None))
        self.label_location.setText(_translate("Dist_Force_Dialog", "Start:", None))
        self.label_magnitude.setText(_translate("Dist_Force_Dialog", "End:", None))
        self.label.setText(_translate("Dist_Force_Dialog", "Magnitude:", None))

