#!/bin/python
# -*- coding: utf-8 -*-
################################################################################
# author: Lex Li
# version: 1.0
################################################################################

import sys
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        widget = QWidget()

        topTab = QTabWidget()
        subTab = QTabWidget()

        vLayout4Top = QVBoxLayout()
        vLayout4Sub = QVBoxLayout()

        topWidget = QWidget()
        subWidget = QWidget()

        # 设置子tab
        subTab.addTab(QLabel('收入'), '收入')
        subTab.addTab(QLabel('支出'), '支出')
        subTab.addTab(QLabel('加班报销'), '加班报销')
        subTab.addTab(QLabel('余额宝'), '余额宝')

        vLayout4Sub.addWidget(subTab)

        topWidget.setLayout(vLayout4Sub)

        vLayout4Top.addWidget(topWidget)

        widget.setLayout(vLayout4Top)

        topTab.addTab(widget, '财务管理')
        topTab.addTab(QWidget(), 'ebook')
        # 个人财务管理 '财务管理'



        '''
        vLayout11 = QVBoxLayout()
        #vLayout11.addWidget(label10)
        widget11 = QWidget()
        widget11.setLayout(vLayout11)
        subTab.addTab(widget11, '收入')

        widget1 = QWidget()
        vLayout11.addWidget(subTab)
        widget1.setLayout(vLayout11)
        topTab.addTab(widget1, '个人财务')

        topWidget = QWidget()
        vLayout4Top.addWidget()
        '''

        hLayout = QHBoxLayout()
        hLayout.addWidget(topTab)
        self.setLayout(hLayout)
        self.setWindowTitle('个人管理系统')
        self.resize(800, 600)


def main():
    app = QApplication(sys.argv)
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

        # 个人ebook管理
        #label2 = QLabel('ebook')

        #label21 = QLabel('PDF')
        #label22 = QLabel('Mobi')
        #label23 = QLabel('ePub')
        #label24 = QLabel('TXT')