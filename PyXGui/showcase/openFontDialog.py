# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        button = QPushButton('Dialog', self)
        button.setFocusPolicy(Qt.NoFocus)
        button.move(20, 20)

        hbox.addWidget(button)

        button.clicked.connect(self.showDialog)

        self.label = QLabel('Knowledge only matters', self)
        self.label.move(130, 20)

        hbox.addWidget(self.label, 1)
        self.setLayout(hbox)

        self.setWindowTitle('FontDialog')
        self.setGeometry(300, 300, 250, 110)

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())