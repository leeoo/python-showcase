# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customTitleBar.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 931, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.titleBarLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleBarLabel.setGeometry(QtCore.QRect(0, 0, 921, 20))
        self.titleBarLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleBarLabel.setObjectName("titleBarLabel")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(895, -1, 30, 20))
        self.closeButton.setMinimumSize(QtCore.QSize(30, 20))
        self.closeButton.setMaximumSize(QtCore.QSize(25, 20))
        self.closeButton.setBaseSize(QtCore.QSize(10, 10))
        self.closeButton.setObjectName("closeButton")
        self.minButton = QtWidgets.QPushButton(self.centralwidget)
        self.minButton.setGeometry(QtCore.QRect(839, -1, 30, 20))
        self.minButton.setMinimumSize(QtCore.QSize(30, 20))
        self.minButton.setMaximumSize(QtCore.QSize(25, 20))
        self.minButton.setBaseSize(QtCore.QSize(10, 10))
        self.minButton.setObjectName("minButton")
        self.maxButton = QtWidgets.QPushButton(self.centralwidget)
        self.maxButton.setGeometry(QtCore.QRect(867, -1, 30, 20))
        self.maxButton.setMinimumSize(QtCore.QSize(30, 20))
        self.maxButton.setMaximumSize(QtCore.QSize(25, 20))
        self.maxButton.setBaseSize(QtCore.QSize(10, 10))
        self.maxButton.setObjectName("maxButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.titleBarLabel.setText(_translate("MainWindow", "TextLabel"))
        self.closeButton.setText(_translate("MainWindow", "X"))
        self.minButton.setText(_translate("MainWindow", "-"))
        self.maxButton.setText(_translate("MainWindow", "+"))

