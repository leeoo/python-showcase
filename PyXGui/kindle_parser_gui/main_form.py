# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created: Mon Dec  1 18:53:15 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 771, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.directoryNameEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.directoryNameEdit.setObjectName("directoryNameEdit")
        self.horizontalLayout_2.addWidget(self.directoryNameEdit)
        self.selectDirectory = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.selectDirectory.setObjectName("selectDirectory")
        self.horizontalLayout_2.addWidget(self.selectDirectory)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 771, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filenameEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.filenameEdit.setObjectName("filenameEdit")
        self.horizontalLayout_3.addWidget(self.filenameEdit)
        self.selectFile = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.selectFile.setObjectName("selectFile")
        self.horizontalLayout_3.addWidget(self.selectFile)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(480, 510, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.selectFiles = QtWidgets.QPushButton(self.centralwidget)
        self.selectFiles.setGeometry(QtCore.QRect(470, 160, 75, 23))
        self.selectFiles.setObjectName("selectFiles")
        self.fileListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.fileListWidget.setGeometry(QtCore.QRect(10, 150, 451, 301))
        self.fileListWidget.setObjectName("fileListWidget")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kindle parser GUI - epub to azw"))
        self.selectDirectory.setText(_translate("MainWindow", "选择文件夹..."))
        self.selectFile.setText(_translate("MainWindow", "选择文件..."))
        self.selectFiles.setText(_translate("MainWindow", "选择多文件"))

