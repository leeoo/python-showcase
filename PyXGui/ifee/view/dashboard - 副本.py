# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created: Sat Jun 28 17:19:11 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dashboardTabWidget(object):
    def setupUi(self, dashboardTabWidget):
        dashboardTabWidget.setObjectName("dashboardTabWidget")
        dashboardTabWidget.resize(960, 720)
        self.feeManageTab = QtWidgets.QWidget()
        self.feeManageTab.setObjectName("feeManageTab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.feeManageTab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.feeManageTabWidget = QtWidgets.QTabWidget(self.feeManageTab)
        self.feeManageTabWidget.setObjectName("feeManageTabWidget")
        self.incomeTab = QtWidgets.QWidget()
        self.incomeTab.setObjectName("incomeTab")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.incomeTab)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.incomeTableView = QtWidgets.QTableView(self.incomeTab)
        self.incomeTableView.setObjectName("incomeTableView")
        self.horizontalLayout_6.addWidget(self.incomeTableView)
        self.feeManageTabWidget.addTab(self.incomeTab, "")
        self.paymentTab = QtWidgets.QWidget()
        self.paymentTab.setObjectName("paymentTab")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.paymentTab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.paymentTableView = QtWidgets.QTableView(self.paymentTab)
        self.paymentTableView.setObjectName("paymentTableView")
        self.horizontalLayout_7.addWidget(self.paymentTableView)
        self.feeManageTabWidget.addTab(self.paymentTab, "")
        self.overtimeTab = QtWidgets.QWidget()
        self.overtimeTab.setObjectName("overtimeTab")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.overtimeTab)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.overtimeTableView = QtWidgets.QTableView(self.overtimeTab)
        self.overtimeTableView.setObjectName("overtimeTableView")
        self.horizontalLayout_8.addWidget(self.overtimeTableView)
        self.feeManageTabWidget.addTab(self.overtimeTab, "")
        self.yuEBaoTab = QtWidgets.QWidget()
        self.yuEBaoTab.setObjectName("yuEBaoTab")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.yuEBaoTab)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.yuEBaoTableView = QtWidgets.QTableView(self.yuEBaoTab)
        self.yuEBaoTableView.setObjectName("yuEBaoTableView")
        self.horizontalLayout_9.addWidget(self.yuEBaoTableView)
        self.feeManageTabWidget.addTab(self.yuEBaoTab, "")
        self.horizontalLayout_5.addWidget(self.feeManageTabWidget)
        dashboardTabWidget.addTab(self.feeManageTab, "")
        self.bookManageTab = QtWidgets.QWidget()
        self.bookManageTab.setObjectName("bookManageTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bookManageTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.bookManageTab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.bookManageTab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.bookManageTab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.bookManageTab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.bookManageTab)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.bookManageTab)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.bookManageTab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.bookManageTab)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.bookManageTab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.bookManageTab)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.label_15 = QtWidgets.QLabel(self.bookManageTab)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.comboBox_2 = QtWidgets.QComboBox(self.bookManageTab)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.bookManageTab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.bookManageTabWidget = QtWidgets.QTabWidget(self.bookManageTab)
        self.bookManageTabWidget.setObjectName("bookManageTabWidget")
        self.bookTab = QtWidgets.QWidget()
        self.bookTab.setObjectName("bookTab")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.bookTab)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.bookTableView = QtWidgets.QTableView(self.bookTab)
        self.bookTableView.setObjectName("bookTableView")
        self.horizontalLayout_10.addWidget(self.bookTableView)
        self.bookManageTabWidget.addTab(self.bookTab, "")
        self.verticalLayout_2.addWidget(self.bookManageTabWidget)
        dashboardTabWidget.addTab(self.bookManageTab, "")
        self.accountManageTab = QtWidgets.QWidget()
        self.accountManageTab.setObjectName("accountManageTab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.accountManageTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.accountTabWidget = QtWidgets.QTabWidget(self.accountManageTab)
        self.accountTabWidget.setObjectName("accountTabWidget")
        self.accountTab = QtWidgets.QWidget()
        self.accountTab.setObjectName("accountTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.accountTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.newButton = QtWidgets.QPushButton(self.accountTab)
        self.newButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.newButton.setObjectName("newButton")
        self.horizontalLayout_14.addWidget(self.newButton)
        self.refreshButton = QtWidgets.QPushButton(self.accountTab)
        self.refreshButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_14.addWidget(self.refreshButton)
        self.importButton = QtWidgets.QPushButton(self.accountTab)
        self.importButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.importButton.setObjectName("importButton")
        self.horizontalLayout_14.addWidget(self.importButton)
        self.exportButton = QtWidgets.QPushButton(self.accountTab)
        self.exportButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout_14.addWidget(self.exportButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.useridLabel = QtWidgets.QLabel(self.accountTab)
        self.useridLabel.setObjectName("useridLabel")
        self.horizontalLayout_3.addWidget(self.useridLabel)
        self.useridLineEdit = QtWidgets.QLineEdit(self.accountTab)
        self.useridLineEdit.setObjectName("useridLineEdit")
        self.horizontalLayout_3.addWidget(self.useridLineEdit)
        self.usernameLabel = QtWidgets.QLabel(self.accountTab)
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout_3.addWidget(self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.accountTab)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.horizontalLayout_3.addWidget(self.usernameLineEdit)
        self.emailLabel = QtWidgets.QLabel(self.accountTab)
        self.emailLabel.setObjectName("emailLabel")
        self.horizontalLayout_3.addWidget(self.emailLabel)
        self.emailLineEdit = QtWidgets.QLineEdit(self.accountTab)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.horizontalLayout_3.addWidget(self.emailLineEdit)
        self.phoneNoLabel = QtWidgets.QLabel(self.accountTab)
        self.phoneNoLabel.setObjectName("phoneNoLabel")
        self.horizontalLayout_3.addWidget(self.phoneNoLabel)
        self.phoneNoLineEdit = QtWidgets.QLineEdit(self.accountTab)
        self.phoneNoLineEdit.setObjectName("phoneNoLineEdit")
        self.horizontalLayout_3.addWidget(self.phoneNoLineEdit)
        self.registYearLabel = QtWidgets.QLabel(self.accountTab)
        self.registYearLabel.setObjectName("registYearLabel")
        self.horizontalLayout_3.addWidget(self.registYearLabel)
        self.registYearComboBox = QtWidgets.QComboBox(self.accountTab)
        self.registYearComboBox.setObjectName("registYearComboBox")
        self.horizontalLayout_3.addWidget(self.registYearComboBox)
        self.searchButton = QtWidgets.QPushButton(self.accountTab)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_3.addWidget(self.searchButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(self.accountTab)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.accountTabWidget.addTab(self.accountTab, "")
        self.accountEditTab = QtWidgets.QWidget()
        self.accountEditTab.setObjectName("accountEditTab")
        self.formLayoutWidget = QtWidgets.QWidget(self.accountEditTab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(370, 80, 361, 421))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.radioButton_3)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.dateEdit_2)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.accountTabWidget.addTab(self.accountEditTab, "")
        self.horizontalLayout_4.addWidget(self.accountTabWidget)
        dashboardTabWidget.addTab(self.accountManageTab, "")
        self.favoritesManageTab = QtWidgets.QWidget()
        self.favoritesManageTab.setObjectName("favoritesManageTab")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.favoritesManageTab)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.favoritesTabWidget = QtWidgets.QTabWidget(self.favoritesManageTab)
        self.favoritesTabWidget.setObjectName("favoritesTabWidget")
        self.favoriteSiteTab = QtWidgets.QWidget()
        self.favoriteSiteTab.setObjectName("favoriteSiteTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.favoriteSiteTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.newButton_3 = QtWidgets.QPushButton(self.favoriteSiteTab)
        self.newButton_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.newButton_3.setObjectName("newButton_3")
        self.horizontalLayout_16.addWidget(self.newButton_3)
        self.refreshButton_3 = QtWidgets.QPushButton(self.favoriteSiteTab)
        self.refreshButton_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.refreshButton_3.setObjectName("refreshButton_3")
        self.horizontalLayout_16.addWidget(self.refreshButton_3)
        self.importButton_3 = QtWidgets.QPushButton(self.favoriteSiteTab)
        self.importButton_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.importButton_3.setObjectName("importButton_3")
        self.horizontalLayout_16.addWidget(self.importButton_3)
        self.exportButton_3 = QtWidgets.QPushButton(self.favoriteSiteTab)
        self.exportButton_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.exportButton_3.setObjectName("exportButton_3")
        self.horizontalLayout_16.addWidget(self.exportButton_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.useridLabel_3 = QtWidgets.QLabel(self.favoriteSiteTab)
        self.useridLabel_3.setObjectName("useridLabel_3")
        self.horizontalLayout_17.addWidget(self.useridLabel_3)
        self.useridLineEdit_3 = QtWidgets.QLineEdit(self.favoriteSiteTab)
        self.useridLineEdit_3.setObjectName("useridLineEdit_3")
        self.horizontalLayout_17.addWidget(self.useridLineEdit_3)
        self.usernameLabel_3 = QtWidgets.QLabel(self.favoriteSiteTab)
        self.usernameLabel_3.setObjectName("usernameLabel_3")
        self.horizontalLayout_17.addWidget(self.usernameLabel_3)
        self.usernameLineEdit_3 = QtWidgets.QLineEdit(self.favoriteSiteTab)
        self.usernameLineEdit_3.setObjectName("usernameLineEdit_3")
        self.horizontalLayout_17.addWidget(self.usernameLineEdit_3)
        self.emailLabel_3 = QtWidgets.QLabel(self.favoriteSiteTab)
        self.emailLabel_3.setObjectName("emailLabel_3")
        self.horizontalLayout_17.addWidget(self.emailLabel_3)
        self.emailLineEdit_3 = QtWidgets.QLineEdit(self.favoriteSiteTab)
        self.emailLineEdit_3.setObjectName("emailLineEdit_3")
        self.horizontalLayout_17.addWidget(self.emailLineEdit_3)
        self.phoneNoLabel_3 = QtWidgets.QLabel(self.favoriteSiteTab)
        self.phoneNoLabel_3.setObjectName("phoneNoLabel_3")
        self.horizontalLayout_17.addWidget(self.phoneNoLabel_3)
        self.phoneNoLineEdit_3 = QtWidgets.QLineEdit(self.favoriteSiteTab)
        self.phoneNoLineEdit_3.setObjectName("phoneNoLineEdit_3")
        self.horizontalLayout_17.addWidget(self.phoneNoLineEdit_3)
        self.searchButton_3 = QtWidgets.QPushButton(self.favoriteSiteTab)
        self.searchButton_3.setObjectName("searchButton_3")
        self.horizontalLayout_17.addWidget(self.searchButton_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.favoriteSiteTab)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.verticalLayout_3.addWidget(self.tableWidget_3)
        self.favoritesTabWidget.addTab(self.favoriteSiteTab, "")
        self.favoriteBookTab = QtWidgets.QWidget()
        self.favoriteBookTab.setObjectName("favoriteBookTab")
        self.favoritesTabWidget.addTab(self.favoriteBookTab, "")
        self.horizontalLayout_12.addWidget(self.favoritesTabWidget)
        dashboardTabWidget.addTab(self.favoritesManageTab, "")
        self.todoManageTab = QtWidgets.QWidget()
        self.todoManageTab.setObjectName("todoManageTab")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.todoManageTab)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(self.todoManageTab)
        self.tabWidget.setObjectName("tabWidget")
        self.designAndDevTab = QtWidgets.QWidget()
        self.designAndDevTab.setObjectName("designAndDevTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.designAndDevTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.designAndDevTab)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.listWidget = QtWidgets.QListWidget(self.designAndDevTab)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_4.addWidget(self.listWidget)
        self.treeWidget = QtWidgets.QTreeWidget(self.designAndDevTab)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.designAndDevTab, "")
        self.unreadBookTab = QtWidgets.QWidget()
        self.unreadBookTab.setObjectName("unreadBookTab")
        self.tabWidget.addTab(self.unreadBookTab, "")
        self.unwatchVideoTab = QtWidgets.QWidget()
        self.unwatchVideoTab.setObjectName("unwatchVideoTab")
        self.tabWidget.addTab(self.unwatchVideoTab, "")
        self.horizontalLayout_11.addWidget(self.tabWidget)
        dashboardTabWidget.addTab(self.todoManageTab, "")

        self.retranslateUi(dashboardTabWidget)
        dashboardTabWidget.setCurrentIndex(4)
        self.feeManageTabWidget.setCurrentIndex(3)
        self.bookManageTabWidget.setCurrentIndex(0)
        self.accountTabWidget.setCurrentIndex(0)
        self.favoritesTabWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dashboardTabWidget)

    def retranslateUi(self, dashboardTabWidget):
        _translate = QtCore.QCoreApplication.translate
        dashboardTabWidget.setWindowTitle(_translate("dashboardTabWidget", "个人管理系统"))
        self.feeManageTabWidget.setTabText(self.feeManageTabWidget.indexOf(self.incomeTab), _translate("dashboardTabWidget", "收入"))
        self.feeManageTabWidget.setTabText(self.feeManageTabWidget.indexOf(self.paymentTab), _translate("dashboardTabWidget", "支出"))
        self.feeManageTabWidget.setTabText(self.feeManageTabWidget.indexOf(self.overtimeTab), _translate("dashboardTabWidget", "加班报销"))
        self.feeManageTabWidget.setTabText(self.feeManageTabWidget.indexOf(self.yuEBaoTab), _translate("dashboardTabWidget", "余额宝"))
        dashboardTabWidget.setTabText(dashboardTabWidget.indexOf(self.feeManageTab), _translate("dashboardTabWidget", "财务管理"))
        self.pushButton_4.setText(_translate("dashboardTabWidget", "New"))
        self.pushButton_3.setText(_translate("dashboardTabWidget", "Refresh"))
        self.pushButton_2.setText(_translate("dashboardTabWidget", "Import"))
        self.pushButton.setText(_translate("dashboardTabWidget", "Export"))
        self.label.setText(_translate("dashboardTabWidget", "Book Name"))
        self.label_2.setText(_translate("dashboardTabWidget", "Author"))
        self.label_3.setText(_translate("dashboardTabWidget", "Book Type"))
        self.comboBox.setItemText(0, _translate("dashboardTabWidget", "All"))
        self.comboBox.setItemText(1, _translate("dashboardTabWidget", "纸质"))
        self.comboBox.setItemText(2, _translate("dashboardTabWidget", "Mobi"))
        self.comboBox.setItemText(3, _translate("dashboardTabWidget", "ePub"))
        self.comboBox.setItemText(4, _translate("dashboardTabWidget", "PDF"))
        self.comboBox.setItemText(5, _translate("dashboardTabWidget", "TXT"))
        self.label_15.setText(_translate("dashboardTabWidget", "Class"))
        self.comboBox_2.setItemText(0, _translate("dashboardTabWidget", "All"))
        self.comboBox_2.setItemText(1, _translate("dashboardTabWidget", "Self-Improvement"))
        self.comboBox_2.setItemText(2, _translate("dashboardTabWidget", "财经"))
        self.comboBox_2.setItemText(3, _translate("dashboardTabWidget", "自然科学"))
        self.comboBox_2.setItemText(4, _translate("dashboardTabWidget", "人文社科"))
        self.comboBox_2.setItemText(5, _translate("dashboardTabWidget", "文学"))
        self.comboBox_2.setItemText(6, _translate("dashboardTabWidget", "漫画"))
        self.comboBox_2.setItemText(7, _translate("dashboardTabWidget", "无类"))
        self.pushButton_5.setText(_translate("dashboardTabWidget", "Search"))
        self.bookManageTabWidget.setTabText(self.bookManageTabWidget.indexOf(self.bookTab), _translate("dashboardTabWidget", "book"))
        dashboardTabWidget.setTabText(dashboardTabWidget.indexOf(self.bookManageTab), _translate("dashboardTabWidget", "book管理"))
        self.newButton.setText(_translate("dashboardTabWidget", "New"))
        self.refreshButton.setText(_translate("dashboardTabWidget", "Refresh"))
        self.importButton.setText(_translate("dashboardTabWidget", "Import"))
        self.exportButton.setText(_translate("dashboardTabWidget", "Export"))
        self.useridLabel.setText(_translate("dashboardTabWidget", "User Id"))
        self.usernameLabel.setText(_translate("dashboardTabWidget", "User Name"))
        self.emailLabel.setText(_translate("dashboardTabWidget", "Email"))
        self.phoneNoLabel.setText(_translate("dashboardTabWidget", "Phone No"))
        self.registYearLabel.setText(_translate("dashboardTabWidget", "Regist Year"))
        self.searchButton.setText(_translate("dashboardTabWidget", "Search"))
        self.tableWidget.setSortingEnabled(False)
        self.accountTabWidget.setTabText(self.accountTabWidget.indexOf(self.accountTab), _translate("dashboardTabWidget", "Account List"))
        self.label_13.setText(_translate("dashboardTabWidget", "User id"))
        self.label_6.setText(_translate("dashboardTabWidget", "Usern ame"))
        self.label_7.setText(_translate("dashboardTabWidget", "Password"))
        self.label_4.setText(_translate("dashboardTabWidget", "Email"))
        self.label_5.setText(_translate("dashboardTabWidget", "Gender"))
        self.radioButton.setText(_translate("dashboardTabWidget", "Male"))
        self.radioButton_2.setText(_translate("dashboardTabWidget", "Female"))
        self.radioButton_3.setText(_translate("dashboardTabWidget", "Keep secrete."))
        self.label_8.setText(_translate("dashboardTabWidget", "Age"))
        self.label_9.setText(_translate("dashboardTabWidget", "Creator"))
        self.label_10.setText(_translate("dashboardTabWidget", "Modifier"))
        self.label_11.setText(_translate("dashboardTabWidget", "Create time"))
        self.label_12.setText(_translate("dashboardTabWidget", "Modification time"))
        self.label_14.setText(_translate("dashboardTabWidget", "Description"))
        self.accountTabWidget.setTabText(self.accountTabWidget.indexOf(self.accountEditTab), _translate("dashboardTabWidget", "Account Edit"))
        dashboardTabWidget.setTabText(dashboardTabWidget.indexOf(self.accountManageTab), _translate("dashboardTabWidget", "用户管理"))
        self.newButton_3.setText(_translate("dashboardTabWidget", "New"))
        self.refreshButton_3.setText(_translate("dashboardTabWidget", "Refresh"))
        self.importButton_3.setText(_translate("dashboardTabWidget", "Import"))
        self.exportButton_3.setText(_translate("dashboardTabWidget", "Export"))
        self.useridLabel_3.setText(_translate("dashboardTabWidget", "Site Name"))
        self.usernameLabel_3.setText(_translate("dashboardTabWidget", "UURL"))
        self.emailLabel_3.setText(_translate("dashboardTabWidget", "Type"))
        self.phoneNoLabel_3.setText(_translate("dashboardTabWidget", "Tag"))
        self.searchButton_3.setText(_translate("dashboardTabWidget", "Search"))
        self.tableWidget_3.setSortingEnabled(False)
        self.favoritesTabWidget.setTabText(self.favoritesTabWidget.indexOf(self.favoriteSiteTab), _translate("dashboardTabWidget", "站点收藏"))
        self.favoritesTabWidget.setTabText(self.favoritesTabWidget.indexOf(self.favoriteBookTab), _translate("dashboardTabWidget", "书籍收藏"))
        dashboardTabWidget.setTabText(dashboardTabWidget.indexOf(self.favoritesManageTab), _translate("dashboardTabWidget", "Favorites"))
        self.checkBox.setText(_translate("dashboardTabWidget", "+ 给各列表页面加上增删改查功能"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("dashboardTabWidget", "aa"))
        item = self.listWidget.item(1)
        item.setText(_translate("dashboardTabWidget", "bb"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("dashboardTabWidget", "1"))
        self.treeWidget.headerItem().setText(1, _translate("dashboardTabWidget", "新建列"))
        self.treeWidget.headerItem().setText(2, _translate("dashboardTabWidget", "a"))
        self.treeWidget.headerItem().setText(3, _translate("dashboardTabWidget", "d"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("dashboardTabWidget", "aa"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("dashboardTabWidget", "bb"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("dashboardTabWidget", "cc"))
        self.treeWidget.topLevelItem(0).setText(3, _translate("dashboardTabWidget", "dd"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("dashboardTabWidget", "11"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("dashboardTabWidget", "ccdd"))
        self.treeWidget.topLevelItem(0).child(0).setText(2, _translate("dashboardTabWidget", "eeff"))
        self.treeWidget.topLevelItem(0).child(0).setText(3, _translate("dashboardTabWidget", "aabbcc"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("dashboardTabWidget", "12"))
        self.treeWidget.topLevelItem(0).child(1).setText(1, _translate("dashboardTabWidget", "1"))
        self.treeWidget.topLevelItem(0).child(1).setText(2, _translate("dashboardTabWidget", "2"))
        self.treeWidget.topLevelItem(0).child(1).setText(3, _translate("dashboardTabWidget", "3"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("dashboardTabWidget", "13"))
        self.treeWidget.topLevelItem(0).child(2).setText(1, _translate("dashboardTabWidget", "23"))
        self.treeWidget.topLevelItem(0).child(2).setText(2, _translate("dashboardTabWidget", "46"))
        self.treeWidget.topLevelItem(0).child(2).setText(3, _translate("dashboardTabWidget", "46"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("dashboardTabWidget", "bb"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("dashboardTabWidget", "asdg"))
        self.treeWidget.topLevelItem(1).setText(2, _translate("dashboardTabWidget", "asdg"))
        self.treeWidget.topLevelItem(1).setText(3, _translate("dashboardTabWidget", "dsgdsg"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.designAndDevTab), _translate("dashboardTabWidget", "设计开发 "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unreadBookTab), _translate("dashboardTabWidget", "待阅书籍"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unwatchVideoTab), _translate("dashboardTabWidget", "待观影视"))
        dashboardTabWidget.setTabText(dashboardTabWidget.indexOf(self.todoManageTab), _translate("dashboardTabWidget", "TODO"))

