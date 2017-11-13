# -*- coding: utf-8 -*-

# PyCharm Python 3.6
#by Lex Li
#on 2017-07-14

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys
import os.path
# import logging
import logging.config
from configparser import ConfigParser


# Define function to import external files when using PyInstaller.
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath('.')
#
#     print('base_path -> %s, relative_path -> %s' % (base_path, relative_path))
#     return os.path.join(base_path, relative_path)

# Works well!
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    print(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
################################
# logging.config.fileConfig(resource_path('config/logging.ini'))
# logging.config.fileConfig(resource_path('logging.ini'))
# logging.config.fileConfig('logging.ini')
log = logging.getLogger(__name__)
log.info("I am logging for testing!!!!!!!!!!!")

try:
    logging.config.fileConfig(resource_path('config/logging.ini'))
except Exception as e:
    # 直接在程序运行时写文件，也能正常运行！这说明可能是logging.config.fileConfig()这里出错了！！！
    test_file = open(resource_path('test_file.txt'), 'w')
    test_file.write('test file 尝试在加载日志配置文件报错时生成一个测试文件！')
    test_file.flush()
    test_file.close()
################################


class AppWindow(QMainWindow):

    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)

        uic.loadUi(resource_path('pyinstaller_demo.ui'), self)

        columns = self.load_config()

        values = [[1, 'Lex', 'Male', 20], [2, 'Li', 'Male', 23]]

        self.handle_ui_action()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)

        row_no = 0
        for row_value in values:
            column_no = 0
            for value in row_value:
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_no, column_no, item)
                column_no += 1
            row_no += 1


    def handle_ui_action(self):
        pass

    def load_config(self):
        config_file = open(resource_path('config.ini'))
        ini_parser = ConfigParser()
        ini_parser.read_file(config_file)
        config_content_sections = ini_parser.sections()

        columns = None

        for section in config_content_sections:
            # log.debug('section -> %s' % section)
            options = ini_parser.options(section)
            for option in options:
                option_value = ini_parser.get(section, option)
                # log.debug('option -> %s, value -> %s' % (option, option_value))
                print('option->%s' % option)
                print('option_value->%s' % option_value)
                columns = option_value.split(',')

        print('columns->%s' % columns)
        return columns


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_window = AppWindow()
    app_window.show()
    sys.exit(app.exec())
