# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/PRACTICUM/project_manager/project_manager_ui.ui'
#
# Created: Thu Feb 18 16:25:24 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.path_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_Label.sizePolicy().hasHeightForWidth())
        self.path_Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_Label.setFont(font)
        self.path_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.path_Label.setObjectName("path_Label")
        self.horizontalLayout_3.addWidget(self.path_Label)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 26))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.path_Button = QtWidgets.QPushButton(self.centralwidget)
        self.path_Button.setMaximumSize(QtCore.QSize(80, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.path_Button.setFont(font)
        self.path_Button.setObjectName("path_Button")
        self.horizontalLayout_3.addWidget(self.path_Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.project_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_Label.sizePolicy().hasHeightForWidth())
        self.project_Label.setSizePolicy(sizePolicy)
        self.project_Label.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.project_Label.setFont(font)
        self.project_Label.setObjectName("project_Label")
        self.horizontalLayout.addWidget(self.project_Label)
        self.project_combo = QtWidgets.QComboBox(self.centralwidget)
        self.project_combo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_combo.sizePolicy().hasHeightForWidth())
        self.project_combo.setSizePolicy(sizePolicy)
        self.project_combo.setMinimumSize(QtCore.QSize(6, 0))
        self.project_combo.setMaximumSize(QtCore.QSize(250, 25))
        self.project_combo.setSizeIncrement(QtCore.QSize(0, 0))
        self.project_combo.setBaseSize(QtCore.QSize(21, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.project_combo.setFont(font)
        self.project_combo.setObjectName("project_combo")
        self.project_combo.addItem("")
        self.horizontalLayout.addWidget(self.project_combo)
        self.newproject = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newproject.sizePolicy().hasHeightForWidth())
        self.newproject.setSizePolicy(sizePolicy)
        self.newproject.setMaximumSize(QtCore.QSize(25, 16777215))
        self.newproject.setObjectName("newproject")
        self.horizontalLayout.addWidget(self.newproject)
        spacerItem = QtWidgets.QSpacerItem(25, 14, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.AssetorShot_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AssetorShot_Label.sizePolicy().hasHeightForWidth())
        self.AssetorShot_Label.setSizePolicy(sizePolicy)
        self.AssetorShot_Label.setMaximumSize(QtCore.QSize(112, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AssetorShot_Label.setFont(font)
        self.AssetorShot_Label.setObjectName("AssetorShot_Label")
        self.horizontalLayout.addWidget(self.AssetorShot_Label)
        self.AssetorShot = QtWidgets.QComboBox(self.centralwidget)
        self.AssetorShot.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AssetorShot.sizePolicy().hasHeightForWidth())
        self.AssetorShot.setSizePolicy(sizePolicy)
        self.AssetorShot.setMinimumSize(QtCore.QSize(6, 0))
        self.AssetorShot.setMaximumSize(QtCore.QSize(250, 25))
        self.AssetorShot.setSizeIncrement(QtCore.QSize(0, 0))
        self.AssetorShot.setBaseSize(QtCore.QSize(21, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AssetorShot.setFont(font)
        self.AssetorShot.setObjectName("AssetorShot")
        self.AssetorShot.addItem("")
        self.AssetorShot.addItem("")
        self.horizontalLayout.addWidget(self.AssetorShot)
        spacerItem1 = QtWidgets.QSpacerItem(25, 14, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.department_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.department_Label.sizePolicy().hasHeightForWidth())
        self.department_Label.setSizePolicy(sizePolicy)
        self.department_Label.setMaximumSize(QtCore.QSize(103, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.department_Label.setFont(font)
        self.department_Label.setObjectName("department_Label")
        self.horizontalLayout.addWidget(self.department_Label)
        self.department_combo = QtWidgets.QComboBox(self.centralwidget)
        self.department_combo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.department_combo.sizePolicy().hasHeightForWidth())
        self.department_combo.setSizePolicy(sizePolicy)
        self.department_combo.setMinimumSize(QtCore.QSize(6, 0))
        self.department_combo.setMaximumSize(QtCore.QSize(150, 25))
        self.department_combo.setSizeIncrement(QtCore.QSize(0, 0))
        self.department_combo.setBaseSize(QtCore.QSize(21, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.department_combo.setFont(font)
        self.department_combo.setObjectName("department_combo")
        self.department_combo.addItem("")
        self.department_combo.addItem("")
        self.horizontalLayout.addWidget(self.department_combo)
        self.newdepartment = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newdepartment.sizePolicy().hasHeightForWidth())
        self.newdepartment.setSizePolicy(sizePolicy)
        self.newdepartment.setMaximumSize(QtCore.QSize(25, 16777215))
        self.newdepartment.setObjectName("newdepartment")
        self.horizontalLayout.addWidget(self.newdepartment)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.task_Label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_Label_2.sizePolicy().hasHeightForWidth())
        self.task_Label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.task_Label_2.setFont(font)
        self.task_Label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.task_Label_2.setObjectName("task_Label_2")
        self.horizontalLayout_2.addWidget(self.task_Label_2)
        self.Task_combo = QtWidgets.QComboBox(self.centralwidget)
        self.Task_combo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Task_combo.sizePolicy().hasHeightForWidth())
        self.Task_combo.setSizePolicy(sizePolicy)
        self.Task_combo.setMinimumSize(QtCore.QSize(6, 0))
        self.Task_combo.setMaximumSize(QtCore.QSize(173, 25))
        self.Task_combo.setSizeIncrement(QtCore.QSize(0, 0))
        self.Task_combo.setBaseSize(QtCore.QSize(21, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Task_combo.setFont(font)
        self.Task_combo.setObjectName("Task_combo")
        self.Task_combo.addItem("")
        self.Task_combo.addItem("")
        self.horizontalLayout_2.addWidget(self.Task_combo)
        self.Newtask = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Newtask.sizePolicy().hasHeightForWidth())
        self.Newtask.setSizePolicy(sizePolicy)
        self.Newtask.setMaximumSize(QtCore.QSize(25, 16777215))
        self.Newtask.setObjectName("Newtask")
        self.horizontalLayout_2.addWidget(self.Newtask)
        spacerItem2 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.workspace = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workspace.sizePolicy().hasHeightForWidth())
        self.workspace.setSizePolicy(sizePolicy)
        self.workspace.setMaximumSize(QtCore.QSize(108, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.workspace.setFont(font)
        self.workspace.setObjectName("workspace")
        self.horizontalLayout_2.addWidget(self.workspace)
        self.publish = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.publish.sizePolicy().hasHeightForWidth())
        self.publish.setSizePolicy(sizePolicy)
        self.publish.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.publish.setFont(font)
        self.publish.setObjectName("publish")
        self.horizontalLayout_2.addWidget(self.publish)
        self.version_combo = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.version_combo.sizePolicy().hasHeightForWidth())
        self.version_combo.setSizePolicy(sizePolicy)
        self.version_combo.setMaximumSize(QtCore.QSize(166, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.version_combo.setFont(font)
        self.version_combo.setObjectName("version_combo")
        self.version_combo.addItem("")
        self.version_combo.addItem("")
        self.version_combo.addItem("")
        self.horizontalLayout_2.addWidget(self.version_combo)
        spacerItem3 = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Listitem = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Listitem.sizePolicy().hasHeightForWidth())
        self.Listitem.setSizePolicy(sizePolicy)
        self.Listitem.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Listitem.setFont(font)
        self.Listitem.setObjectName("Listitem")
        QtWidgets.QListWidgetItem(self.Listitem)
        QtWidgets.QListWidgetItem(self.Listitem)
        self.verticalLayout.addWidget(self.Listitem)
        self.newAssetorShot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newAssetorShot.sizePolicy().hasHeightForWidth())
        self.newAssetorShot.setSizePolicy(sizePolicy)
        self.newAssetorShot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.newAssetorShot.setObjectName("newAssetorShot")
        self.verticalLayout.addWidget(self.newAssetorShot)
        self.horizontalLayout_13.addLayout(self.verticalLayout)
        self.Listfile = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Listfile.sizePolicy().hasHeightForWidth())
        self.Listfile.setSizePolicy(sizePolicy)
        self.Listfile.setMinimumSize(QtCore.QSize(1, 0))
        self.Listfile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Listfile.setUniformItemSizes(False)
        self.Listfile.setObjectName("Listfile")
        QtWidgets.QListWidgetItem(self.Listfile)
        QtWidgets.QListWidgetItem(self.Listfile)
        QtWidgets.QListWidgetItem(self.Listfile)
        self.horizontalLayout_13.addWidget(self.Listfile)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(300, 200))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)
        self.info.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.verticalLayout_5.addWidget(self.info)
        self.textinfo = QtWidgets.QTextEdit(self.centralwidget)
        self.textinfo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textinfo.sizePolicy().hasHeightForWidth())
        self.textinfo.setSizePolicy(sizePolicy)
        self.textinfo.setMaximumSize(QtCore.QSize(309, 137))
        self.textinfo.setObjectName("textinfo")
        self.verticalLayout_5.addWidget(self.textinfo)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_button.sizePolicy().hasHeightForWidth())
        self.import_button.setSizePolicy(sizePolicy)
        self.import_button.setMaximumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.import_button.setFont(font)
        self.import_button.setObjectName("import_button")
        self.horizontalLayout_11.addWidget(self.import_button)
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setMaximumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_button.setFont(font)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_11.addWidget(self.open_button)
        self.ref_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_button.sizePolicy().hasHeightForWidth())
        self.ref_button.setSizePolicy(sizePolicy)
        self.ref_button.setMaximumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ref_button.setFont(font)
        self.ref_button.setObjectName("ref_button")
        self.horizontalLayout_11.addWidget(self.ref_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setMaximumSize(QtCore.QSize(325, 100))
        self.save.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.verticalLayout_5.addWidget(self.save)
        self.update_combo = QtWidgets.QComboBox(self.centralwidget)
        self.update_combo.setObjectName("update_combo")
        self.update_combo.addItem("")
        self.update_combo.addItem("")
        self.verticalLayout_5.addWidget(self.update_combo)
        self.publish_button = QtWidgets.QPushButton(self.centralwidget)
        self.publish_button.setMaximumSize(QtCore.QSize(325, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.publish_button.setFont(font)
        self.publish_button.setObjectName("publish_button")
        self.verticalLayout_5.addWidget(self.publish_button)
        self.horizontalLayout_13.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.path_Label.setText(QtWidgets.QApplication.translate("MainWindow", "Path :", None, -1))
        self.textEdit.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.path_Button.setText(QtWidgets.QApplication.translate("MainWindow", "Set Path", None, -1))
        self.project_Label.setText(QtWidgets.QApplication.translate("MainWindow", "Project :", None, -1))
        self.project_combo.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "projectA", None, -1))
        self.newproject.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.AssetorShot_Label.setText(QtWidgets.QApplication.translate("MainWindow", "Asset or Shot :", None, -1))
        self.AssetorShot.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Asset", None, -1))
        self.AssetorShot.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Shot", None, -1))
        self.department_Label.setText(QtWidgets.QApplication.translate("MainWindow", "Department :", None, -1))
        self.department_combo.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Model", None, -1))
        self.department_combo.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Rig", None, -1))
        self.newdepartment.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.task_Label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Task :", None, -1))
        self.Task_combo.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "High", None, -1))
        self.Task_combo.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Mid", None, -1))
        self.Newtask.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.workspace.setText(QtWidgets.QApplication.translate("MainWindow", "Workspace", None, -1))
        self.publish.setText(QtWidgets.QApplication.translate("MainWindow", "Publish", None, -1))
        self.version_combo.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Hero", None, -1))
        self.version_combo.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "v001", None, -1))
        self.version_combo.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "v002", None, -1))
        __sortingEnabled = self.Listitem.isSortingEnabled()
        self.Listitem.setSortingEnabled(False)
        self.Listitem.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "A", None, -1))
        self.Listitem.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "B", None, -1))
        self.Listitem.setSortingEnabled(__sortingEnabled)
        self.newAssetorShot.setText(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        __sortingEnabled = self.Listfile.isSortingEnabled()
        self.Listfile.setSortingEnabled(False)
        self.Listfile.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "File 1", None, -1))
        self.Listfile.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "File 2", None, -1))
        self.Listfile.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "File 3", None, -1))
        self.Listfile.setSortingEnabled(__sortingEnabled)
        self.info.setText(QtWidgets.QApplication.translate("MainWindow", "Info:", None, -1))
        self.import_button.setText(QtWidgets.QApplication.translate("MainWindow", "Import", None, -1))
        self.open_button.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.ref_button.setText(QtWidgets.QApplication.translate("MainWindow", "Ref", None, -1))
        self.save.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.update_combo.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Update", None, -1))
        self.update_combo.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Final", None, -1))
        self.publish_button.setText(QtWidgets.QApplication.translate("MainWindow", "Publish", None, -1))

