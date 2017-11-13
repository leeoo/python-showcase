__author__ = 'Lex'

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class BoxLayout(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('box layout')
        ok = QPushButton('Ok')
        cancel = QPushButton('Cancel')

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(ok)
        # hbox.addWidget(cancel)

        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        # self.setLayout(vbox)

        vbox.addWidget(ok)
        vbox.addWidget(cancel)
        self.setLayout(vbox)

        self.resize(600, 400)

app = QApplication(sys.argv)

qb = BoxLayout()
qb.show()
sys.exit(app.exec())
