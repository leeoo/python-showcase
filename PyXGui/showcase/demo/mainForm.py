# -*- coding: utf-8 -*-

#from PyQt4 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class MainForm(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.initUI()

    def initUI(self):
        
#        self.setGeometry(300, 200, 800, 600)
        self.resize(800, 600)
        self.centerInScreen()
        self.setWindowTitle('Kindle电子书管理系统 - Dashboard')
        self.setWindowIcon(QIcon('image/logo.png'))

        self.quitButton = QPushButton('退出(&C)', self)
        self.quitButton.setGeometry(10, 10, 50, 25)
        
        self.changeWindowTitleButton = QPushButton('改变窗体标题', self)
        self.changeWindowTitleButton.setGeometry(80, 10, 50 * 2, 25)
        
        self.labelChangeButton = QPushButton('按钮文本', self)
        self.labelChangeButton.setGeometry(200, 10, 100, 25)
        
        self.showDataButton = QPushButton('数据展示', self)
        self.showDataButton.setGeometry(300, 10, 100, 25)
        
        self.loginButton = QPushButton('登录', self)
        self.loginButton.setGeometry(400, 10, 64, 25)
        
        self.resetButton = QPushButton('重置', self)
        self.resetButton.setGeometry(500, 10, 64, 25)

        # 使用框布局
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.quitButton)
        hbox.addWidget(self.changeWindowTitleButton)
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
#    def sinTest(self):
#        self.connect(self.quitButton, QtCore.SIGNAL('clicked()'), qApp, QtCore.SLOT('quit()'))

    # 重新实现QWidget的QCloseEvent事件对应的closeEvent()方法来改变其默认行为(关闭QWidget时将会产生一个QCloseEvent事件)
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quite?', 
            QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def centerInScreen(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def changeTitle(self):
        self.setWindowTitle('窗体标题改变了！')

    def changeButtonLabel(self):
        self.labelChangeButton.setText('按钮文本改变')


    def handleAction(self):
        self.handleButtonClickAction()

    def reset(self):
        self.resize(800, 600)
        self.centerInScreen()
        self.setWindowTitle('Kindle电子书管理系统 - Dashboard')
        self.labelChangeButton.setText('按钮文本')

# ---------------------------------------------------------------------------------------
    def handleButtonClickAction(self):
        self.handleClickWindowTitleChangeButton()
        self.handleClickQuitButton()
        self.handleClickChangeButtonTextButton()
        self.handleClickResetButton()
        self.handleClickLoginButton()
        self.handleShowDataViewButton()

    
    def handleClickWindowTitleChangeButton(self):
        # 按钮changeWindowTitleButton的内置信号连接名为changeTitle的槽
        self.changeWindowTitleButton.clicked.connect(self.changeTitle)

    def handleClickQuitButton(self):
        self.quitButton.clicked.connect(self.close)

    def handleClickChangeButtonTextButton(self):
        self.labelChangeButton.clicked.connect(self.changeButtonLabel)

    def handleClickLoginButton(self):
        self.loginButton.clicked.connect(self.showLoginForm)

    def handleClickResetButton(self):
        self.resetButton.clicked.connect(self.reset)

    def handleShowDataViewButton(self):
        self.showDataButton.clicked.connect(self.showDataWindow)

# ---------------------------------------------------------------------------------------

    def showLoginForm(self):
        loginForm = QMainWindow(self)
        userid = QLabel('Userid', loginForm)
        password = QLabel('Password', loginForm)
#        password.setGeometry(50, 30, 50, 50)
        comment = QLabel('comment', loginForm)
        
        useridEdit = QLineEdit(loginForm)
        passwordEdit = QLineEdit(loginForm)
        commentEdit = QTextEdit(loginForm)
        
        grid = QGridLayout(loginForm)
        grid.setSpacing(10)
        
        grid.addWidget(userid, 1, 0)
        grid.addWidget(useridEdit, 1, 1)
        grid.addWidget(password, 2, 0)
        grid.addWidget(passwordEdit, 2, 1)
        grid.addWidget(comment, 3, 0)
        grid.addWidget(commentEdit, 3, 1, 5, 1)

        # 参考http://blog.csdn.net/qwk7267936/article/details/6061206
        widget = QWidget(loginForm)
        widget.setLayout(grid)
        loginForm.setCentralWidget(widget)
        
#        loginForm.setLayout(grid)

        loginForm.setWindowTitle('grid layout')
        loginForm.resize(350, 300)
        loginForm.show()


    def showDataWindow(self):
        dataWindow = QMainWindow(self)
        dataWindow.setWindowTitle('Show data view')
        dataWindow.resize(400, 300)
        menubar = dataWindow.menuBar()
        statusbar = dataWindow.statusBar()
        
        exit = QAction(QIcon('icons/default/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit Show Data Window')
        exit.triggered.connect(dataWindow.close)
        
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exit)
        editMenu = menubar.addMenu('&Edit')
        viewMenu = menubar.addMenu('&View')
        
        dataWindow.exit = QAction(QIcon('icons/default/exit.png'), 'Exit', dataWindow)
        dataWindow.exit.setShortcut('Ctrl+Q')
        dataWindow.exit.triggered.connect(dataWindow.close)
        dataWindow.toolbar = dataWindow.addToolBar('Exit')
        dataWindow.toolbar.addAction(dataWindow.exit)
        
        textEdit = QTextEdit()
        dataWindow.setCentralWidget(textEdit)
        dataWindow.show()


class LoginForm(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('登录')
        self.resize(300, 150)
        
        self.username = QLabel('用户名')
        self.password = QLabel('密码')
        self.usernameEdit = QLineEdit()
        self.usernameEdit.setPlaceholderText('请输入用户名')
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setPlaceholderText('请输入密码')
        self.loginButton = QPushButton('登录')
        self.cancelButton = QPushButton('取消')
        
#        gridLayout = QGridLayout()
#        gridLayout.addWidget(self.username, 0, 0)
#        gridLayout.addWidget(self.usernameEdit, 0, 1)
#        gridLayout.addWidget(self.password, 1, 0)
#        gridLayout.addWidget(self.passwordEdit, 1, 1)
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
#        hbox.addStretch(1)
#        hbox2.addStretch(1)
        hbox.addWidget(self.username)
        hbox.addWidget(self.usernameEdit)
        hbox2.addWidget(self.password)
        hbox2.addWidget(self.passwordEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        
        spacerItem = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vbox.addItem(spacerItem)
        
        buttonLayout = QHBoxLayout()
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        buttonLayout.addItem(spacerItem2)
        buttonLayout.addWidget(self.loginButton)
        buttonLayout.addWidget(self.cancelButton)

        vbox.addLayout(buttonLayout)

#        gridLayout.addWidget(self.loginButton, 2, 0)
#        gridLayout.addWidget(self.cancelButton, 2, 1)
        self.setLayout(vbox)
        
        self.loginButton.clicked.connect(self.login)
        self.cancelButton.clicked.connect(self.close) # self.reject

    def login(self):
        if self.usernameEdit.text() == 'admin' and self.passwordEdit.text() == '123456':
            self.accept() # 关闭对话框并返回1
        else:
            QMessageBox.critical(self, '登录失败', '用户名密码不匹配')


def login():
    loginForm = LoginForm()
    if loginForm.exec():
        return True
    else:
        return False


def main():
    app = QApplication(sys.argv)
    
    if login():
        mainForm = MainForm()
        mainForm.handleAction()
        mainForm.show()

        sys.exit(app.exec())

if __name__ == '__main__':
    main()
