# -*- coding: utf-8 -*-

# QInputDialog

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton('Dialog', self)
        
        self.button.setFocusPolicy(Qt.NoFocus)
        self.button.move(20, 20)
        self.button.clicked.connect(self.showDialog)
        self.setFocus()
        
        self.label = QLineEdit(self)
        self.label.move(130, 22)
        
        self.setWindowTitle('InputDialog')
        self.setGeometry(300, 300, 350, 80)


    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.label.setText(str(text))


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
