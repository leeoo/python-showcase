# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Checkbox')

        self.cb = QCheckBox('Show title', self)
        self.cb.setFocusPolicy(Qt.NoFocus)
        self.cb.move(10, 10)
        self.cb.toggle()
        self.cb.stateChanged.connect(self.changeTitle)

    def changeTitle(self, value):

        if self.cb.isChecked():
            self.setWindowTitle('Checkbox')
        else:
            self.setWindowTitle('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
