# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guistructure.ui'
#
# Created: Sat Jul 19 18:12:02 2014
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

class Ui_Beam(object):
    def setupUi(self, Beam):
        Beam.setObjectName(_fromUtf8("Beam"))
        Beam.resize(803, 415)
        self.horizontalLayout = QtGui.QHBoxLayout(Beam)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setSpacing(6)
        self.horizontalLayout_1.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_1.addLayout(self.verticalLayout_3)
        self.verticalLayout_1 = QtGui.QVBoxLayout()
        self.verticalLayout_1.setSpacing(6)
        self.verticalLayout_1.setObjectName(_fromUtf8("verticalLayout_1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_force = QtGui.QPushButton(Beam)
        self.pushButton_force.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_force.sizePolicy().hasHeightForWidth())
        self.pushButton_force.setSizePolicy(sizePolicy)
        self.pushButton_force.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_force.setObjectName(_fromUtf8("pushButton_force"))
        self.verticalLayout_2.addWidget(self.pushButton_force)
        self.pushButton_moment = QtGui.QPushButton(Beam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_moment.sizePolicy().hasHeightForWidth())
        self.pushButton_moment.setSizePolicy(sizePolicy)
        self.pushButton_moment.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_moment.setObjectName(_fromUtf8("pushButton_moment"))
        self.verticalLayout_2.addWidget(self.pushButton_moment)
        self.pushButton_distforce = QtGui.QPushButton(Beam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_distforce.sizePolicy().hasHeightForWidth())
        self.pushButton_distforce.setSizePolicy(sizePolicy)
        self.pushButton_distforce.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_distforce.setObjectName(_fromUtf8("pushButton_distforce"))
        self.verticalLayout_2.addWidget(self.pushButton_distforce)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_1.addLayout(self.horizontalLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_solve = QtGui.QPushButton(Beam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_solve.sizePolicy().hasHeightForWidth())
        self.pushButton_solve.setSizePolicy(sizePolicy)
        self.pushButton_solve.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_solve.setObjectName(_fromUtf8("pushButton_solve"))
        self.horizontalLayout_4.addWidget(self.pushButton_solve)
        self.pushButton_plot = QtGui.QPushButton(Beam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_plot.sizePolicy().hasHeightForWidth())
        self.pushButton_plot.setSizePolicy(sizePolicy)
        self.pushButton_plot.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_plot.setObjectName(_fromUtf8("pushButton_plot"))
        self.horizontalLayout_4.addWidget(self.pushButton_plot)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_1.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.treeWidget = QtGui.QTreeWidget(Beam)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setDefaultSectionSize(75)
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.verticalLayout_1.addLayout(self.horizontalLayout_2)
        self.verticalLayout_1.setStretch(0, 3)
        self.verticalLayout_1.setStretch(1, 1)
        self.verticalLayout_1.setStretch(2, 2)
        self.verticalLayout_1.setStretch(3, 40)
        self.horizontalLayout_1.addLayout(self.verticalLayout_1)
        self.horizontalLayout_1.setStretch(0, 2)
        self.horizontalLayout_1.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.horizontalLayout_1)

        self.retranslateUi(Beam)
        QtCore.QMetaObject.connectSlotsByName(Beam)

    def retranslateUi(self, Beam):
        Beam.setWindowTitle(_translate("Beam", "BeamAnalyzer vAlpha", None))
        self.pushButton_force.setText(_translate("Beam", "Add Force", None))
        self.pushButton_moment.setText(_translate("Beam", "Add Moment", None))
        self.pushButton_distforce.setText(_translate("Beam", "Add Distributed Force", None))
        self.pushButton_solve.setText(_translate("Beam", "Solve", None))
        self.pushButton_plot.setText(_translate("Beam", "Plot", None))
        self.treeWidget.headerItem().setText(0, _translate("Beam", "Type", None))
        self.treeWidget.headerItem().setText(1, _translate("Beam", "Location", None))
        self.treeWidget.headerItem().setText(2, _translate("Beam", "Magnitude", None))
        self.treeWidget.headerItem().setText(3, _translate("Beam", "Known", None))

