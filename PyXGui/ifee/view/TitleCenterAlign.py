# from PyQt5.QtCore import Qt
# # from PyQt5.QtGui import QDockWidget
# from PyQt5.QtGui import QWidget
# from PyQt5.QtCore import QSize
# from PyQt5.QtGui import QPaintEvent
# from PyQt5.QtGui import QStyle
# from PyQt5.QtGui import QPainter
# from PyQt5.QtGui import QMouseEvent
# from PyQt5.QtGui import QMoveEvent
# from PyQt5.QtGui import QLabel
# from PyQt5.QtCore import QRect
# from PyQt5.QtGui import QResizeEvent
# from PyQt5.QtGui import QColor
# from PyQt5.QtCore import QPoint

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyTitleBar(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.floatpix = self.style().standardPixmap(QStyle.SP_TitleBarNormalButton)
        self.titlelabel = QLabel(self);
        # self.titlebar = QStyleOptionTitleBar()
        self.titlelabel.move(self.pos().x() +  self.width()/2 - 25,self.pos().y() + 4)

    def set_title_text(self, text):
        # otb = QStyleOptionTitleBar()
        # otb.SO_TitleBar = 'sdg'
        # self.titlelabel = otb
        self.titlelabel.setText(text)
        # self.titlebar.SO_TitleBar = 'abc'
        # self.titlebar.Type(QStyleOptionTitleBar.SO_TitleBar)

    def paintEvent(self, e):
        painter = QPainter(self)
        rect = self.rect()

        painter.fillRect(rect.left(), rect.top(), rect.width(), rect.height(), QColor(170, 255, 255))
        painter.drawPixmap(rect.topRight() - QPoint(self.floatpix.width() + 10, -8), self.floatpix);
        # painter.drawStaticText(self.titlebar, QColor(255, 255, 255))

QStyle.CC_TitleBar


def main():
    app = QApplication(sys.argv)
    form = MyTitleBar()
    form.set_title_text('hello world')
    form.show()
    sys.exit(app.exec())

if __name__ ==  '__main__':
    main()