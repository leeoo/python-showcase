# -*- coding: utf-8 -*-

import sys
#from PyQt4 import QtGui
from PyQt5.QtWidgets import *


class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self,  windowTitle = 'A simple example for PyQt')
        self.outputArea = QTextBrowser(self)
        self.helloButton = QPushButton(self.trUtf8('问候(&S)'),  self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.outputArea)
        
        self.helloButton.clicked.connect(self.sayHello)
        
    def sayHello(self):
        yourName, okay = QInputDialog.getText(self,  self.trUtf8('请问你的名字是?'),  self.trUtf8('名字'))
        if not okay or yourName == '':
            self.outputArea.append(self.trUtf8('你好，陌生人！'))
        else:
            self.outputArea.append(self.trUtf8('你好，<b>%1</b>。').format(yourName))

app = QApplication(sys.argv)
testWidget = TestWidget()
testWidget.show()
sys.exit(app.exec())
