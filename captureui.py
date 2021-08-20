# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/PRACTICUM/project_manager/captureui.ui'
#
# Created: Wed Feb 17 12:08:13 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Capture(object):
    def setupUi(self, Capture):
        Capture.setObjectName("Capture")
        Capture.setWindowModality(QtCore.Qt.NonModal)
        Capture.resize(677, 460)
        self.verticalLayout = QtWidgets.QVBoxLayout(Capture)
        self.verticalLayout.setObjectName("verticalLayout")
        self.viewport_layout = QtWidgets.QVBoxLayout()
        self.viewport_layout.setObjectName("viewport_layout")
        self.verticalLayout.addLayout(self.viewport_layout)
        self.pushButton = QtWidgets.QPushButton(Capture)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Capture)
        QtCore.QMetaObject.connectSlotsByName(Capture)

    def retranslateUi(self, Capture):
        Capture.setWindowTitle(QtWidgets.QApplication.translate("Capture", "Capture", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Capture", "Capture", None, -1))

