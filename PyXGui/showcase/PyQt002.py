__author__ = 'leeoo'

#from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5 import QtGui
import sys


class TabWidget1(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.setTabsClosable(True)

    def tabInserted(self, index):
        self.tabBar().setVisible(self.count() > 1)

    def tabRemoved(self, index):
        self.tabBar().setVisible(self.count() > 1)
        #self.removeTab(index)



    def initUI(self):
        okButton = QPushButton('ok')
        okButton.move(300, 200)

        self.tabBar = QTabBar()
        self.tabControl = QTabWidget()
        #self.tabControl
        #self.tabBar.addTab(self.tabControl)


        # 使用框布局
        #hbox = QHBoxLayout()
        #hbox.addStretch(1)
        #hbox.addWidget(self.quitButton)
        #hbox.addWidget(self.changeWindowTitleButton)
        #
        #vbox = QVBoxLayout()
        #vbox.addStretch(1)
        #vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)

        hbox.addWidget(self.tabControl)
        hbox.addWidget(self.tabBar)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('test for pyqt')
        self.resize(800, 600)
        self.resize(1440, 900)
        self.resize(720, 450)


def main():
    app = QApplication(sys.argv)
    tab = TabWidget()
    #tab.show()

    #button = QPushButton('Hello')
    #@button.clicked.connect
    #def clicked():
    #    tab.addTab(QLabel('Hello'), 'Hello')
    #
    #@tab.removed.connect
    #def removed(index):
    #    tab.removeTab(index)
    #
    #tab.addTab(button, 'Button')
    #
    #hbox = QHBoxLayout()
    #hbox.addWidget(tab)
    #
    #window = QWidget()
    #window.setLayout(hbox)
    #window.resize(600, 400)
    #window.show()
    sys.exit(app.exec())


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

    def addTab(self, index):
        self.tabBar().setVisible(self.count() > 1)

    def closeTab(self, idx):
        self.removeTab(idx)


if __name__ == '__main__':
    main()
