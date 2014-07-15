# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guistructure.ui'
#
# Created: Mon Jul 14 20:33:55 2014
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

class Ui_Beam_GUI(object):
    def setupUi(self, Beam_GUI):
        Beam_GUI.setObjectName(_fromUtf8("Beam_GUI"))
        Beam_GUI.resize(400, 300)

        self.retranslateUi(Beam_GUI)
        QtCore.QMetaObject.connectSlotsByName(Beam_GUI)

    def retranslateUi(self, Beam_GUI):
        Beam_GUI.setWindowTitle(_translate("Beam_GUI", "BeamAnalyzer vAlpha", None))

