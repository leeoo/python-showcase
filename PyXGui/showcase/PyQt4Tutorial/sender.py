# -*- coding: utf-8 -*-

# 事件发送者

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        button1 = QPushButton('Button 1', self)
        button1.move(30, 50)
        
        button2 = QPushButton('Button 2', self)
        button2.move(150, 50)

        button1.clicked.connect(self.buttonClicked)
        button2.clicked.connect(self.buttonClicked)
        
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Event sender')
        self.resize(290, 150)

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
