__author__ = 'leeoo'

#from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5.QtGui import *
import sys


class MyDialog(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        tabWidget = QTabWidget()

        #新建第一个页面的部件
        widget = QWidget()
        lineEdit = QLineEdit()
        pushButton = QPushButton("Test")
        vLayout = QVBoxLayout()
        vLayout.addWidget(lineEdit)
        vLayout.addWidget(pushButton)
        widget.setLayout(vLayout)


        #新建第二个页面的部件
        label = QLabel("Hello Qt")

        #新建第三个页面的部件
        pushButton3 = QPushButton("Click Me")

        #向QTabWidget中添加第一个页面
        icon1 = QIcon(":/new/icon/images/1.ico")
        tabWidget.addTab(widget, icon1, "Tab1")

        #向QTabWidget中添加第二个页面
        icon2 = QIcon(":/new/icon/images/2.ico")
        tabWidget.addTab(label, icon2, "Tab2")

        #向QTabWidget中添加第三个页面
        icon3 = QIcon(":/new/icon/images/3.ico")
        tabWidget.addTab(pushButton3, icon3, "Tab3")

        layout = QHBoxLayout()
        layout.addWidget(tabWidget)

        self.setLayout(layout)
        self.resize(300, 100)
        self.setWindowTitle("QTabWidgetDemo")


def main():
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
