# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginForm.ui'
#
# Created: Sat Nov  1 19:21:16 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginFormDialog(object):
    def setupUi(self, loginFormDialog):
        loginFormDialog.setObjectName("loginFormDialog")
        loginFormDialog.resize(274, 167)
        self.buttonBox = QtWidgets.QDialogButtonBox(loginFormDialog)
        self.buttonBox.setGeometry(QtCore.QRect(-10, 120, 251, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(loginFormDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 211, 94))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.envComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.envComboBox.setEditable(False)
        self.envComboBox.setMinimumContentsLength(1)
        self.envComboBox.setObjectName("envComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.envComboBox)
        self.labelAlert = QtWidgets.QLabel(loginFormDialog)
        self.labelAlert.setGeometry(QtCore.QRect(30, 150, 201, 16))
        self.labelAlert.setStyleSheet("")
        self.labelAlert.setText("")
        self.labelAlert.setObjectName("labelAlert")

        self.retranslateUi(loginFormDialog)
        self.buttonBox.rejected.connect(loginFormDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(loginFormDialog)

    def retranslateUi(self, loginFormDialog):
        _translate = QtCore.QCoreApplication.translate
        loginFormDialog.setWindowTitle(_translate("loginFormDialog", "Login Form"))
        self.label.setText(_translate("loginFormDialog", "User name"))
        self.label_2.setText(_translate("loginFormDialog", "Password"))
        self.label_4.setText(_translate("loginFormDialog", "Environment"))

