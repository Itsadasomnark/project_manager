# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/PRACTICUM/project_manager/c_dialog.ui'
#
# Created: Mon Feb 15 12:19:07 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class ui_name(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(724, 109)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.filename_edit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.filename_edit.setFont(font)
        self.filename_edit.setObjectName("filename_edit")
        self.horizontalLayout.addWidget(self.filename_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.create = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create.sizePolicy().hasHeightForWidth())
        self.create.setSizePolicy(sizePolicy)
        self.create.setObjectName("create")
        self.verticalLayout.addWidget(self.create)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.name.setText(QtWidgets.QApplication.translate("Dialog", "Name : ", None, -1))
        self.create.setText(QtWidgets.QApplication.translate("Dialog", "create", None, -1))

