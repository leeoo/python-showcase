# -*- coding: utf-8 -*-
# Python 3.3.3
# PyQt 5.1.1
import sys, time, re, urllib.parse, urllib.request, http.cookiejar, json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

RAILWAY_12306 = 'https://kyfw.12306.cn'

"""cookie"""
cookie = http.cookiejar.LWPCookieJar()
#cookie.load('f:/cookie.txt',True,True)
chandle = urllib.request.HTTPCookieProcessor(cookie)

"""获取数据"""


"""ui"""


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        #布局管理器
        # vLayout = QVBoxLayout(self)
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        # self.layout = [QVBoxLayout(self), QHBoxLayout()]
        # self.layout[1].setContentsMargins(0, 0, 0, 0)
        # self.layout[1].setSpacing(0)
        # self.layout[0].setContentsMargins(0, 0, 0, 0)
        # self.layout[0].setSpacing(0)
        # self.layout[0].addLayout(self.layout[1])
        # self.layout = [QVBoxLayout(self), QHBoxLayout()]
        hLayout.setContentsMargins(0, 0, 0, 0)
        hLayout.setSpacing(0)
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)
        vLayout.addLayout(hLayout)

        #输入选项
        queryBarLabels = [QLabel("发站："), QLabel("到站："), QLabel("日期：")]
        # self.queryBar = [QLineEdit(), QLineEdit(), QComboBox()]
        queryBar = [QLineEdit(), QLineEdit(), QComboBox()]
        i = 0
        while i < len(queryBar):
            queryBar[i].setMaximumWidth(100)
            queryBarLabels[i].setMaximumWidth(50)
            queryBarLabels[i].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            hLayout.addWidget(queryBarLabels[i], Qt.AlignRight)
            hLayout.addWidget(queryBar[i], Qt.AlignLeft)
            # self.layout[1].addWidget(queryBarLabels[i], Qt.AlignRight)
            # self.layout[1].addWidget(queryBar[i], Qt.AlignLeft)
            i += 1

        #表格
        # TODO
        head = ['车次', '发站', '到站', '历时', '商务座', '特等座', '一等座', '二等座', '高级软卧', '软卧', '硬卧', '软座', '硬座', '无座', '其他']
        table = QTableWidget()
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setColumnCount(len(head))
        table.setHorizontalHeaderLabels(head)

        okButton = QPushButton("Ok")
        # okButton.clicked.connect(self.submit)

        hLayout.addWidget(okButton)
        vLayout.addWidget(table)

        self.setLayout(vLayout)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(app.exec())