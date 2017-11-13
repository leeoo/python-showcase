__author__ = 'Lex'

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class MessageBox(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('message box')

    # 重写QWidget的默认close事件的处理方法
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QApplication(sys.argv)
msgBox = MessageBox()
msgBox.show()

sys.exit(app.exec())
