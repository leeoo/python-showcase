# -*- encoding:utf-8 -*-

# See: PyQt5 多线程 Signals与Slots http://my.oschina.net/zangzy/blog/172705

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
import threading
import time


class Send(QObject, threading.Thread):
    update_ui = QtCore.pyqtSignal()
    def __init__(self):
        super(Send, self).__init__()

    def run(self):
        while True:
            print("I'm in send function.")
            self.update_ui.emit()
            time.sleep(1)


class Ui_client(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_client, self).__init__(parent)

        self.send_t = Send()

        self.setFixedSize(320, 240)
        self.btn_send = QtWidgets.QPushButton(self)

        self.setWindowTitle('client')
        self.btn_send.setText('send')

        self.btn_send.clicked.connect(self.start_send)
        self.send_t.update_ui.connect(self.client_update)

    def start_send(self):
        self.send_t.start()
        self.send_t.join()

    def client_update(self):
        print("I'm in client_update function.")
        self.btn_send.setText(str(time.time()))
        # print('test..')
        # self.btn_send.setText(str(time.time()))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_client()
    w.show()
    sys.exit(app.exec())
