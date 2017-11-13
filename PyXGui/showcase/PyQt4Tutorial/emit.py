# -*- coding: utf-8 -*-

# 发射信号 | 从QtCore.QObject继承的对象可以发射信号

from PyQt4.QtGui import *
from PyQt4.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

#    def initUI(self):
#        self.closeEmitApp.connect(self.close)
#
#        self.setWindowTitle('emit')
#        self.resize(250, 150)
#
#    def mousePressEvent(self, event):
#        self.emit(self.closeEmitApp)

    def initUI(self):

        self.connect(self, SIGNAL('closeEmitApp()'),
            SLOT('close()'))

        self.setWindowTitle('emit')
        self.resize(250, 150)


    def mousePressEvent(self, event):
        self.emit(SIGNAL('closeEmitApp()'))


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
