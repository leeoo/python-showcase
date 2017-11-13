# -*- coding: utf-8 -*-

# 重新实现事件处理程序

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.setWindowTitle('Escape')
        self.resize(250, 150)

    # 重新实现key press event事件的处理方法
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
