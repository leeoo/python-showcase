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
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    print('base_path -> %s, relative_path -> %s' % (base_path, relative_path))
    return os.path.join(base_path, relative_path)

################################
# logging.config.fileConfig(resource_path('./config/logging.ini'))
# logging.config.fileConfig(resource_path('logging.ini'))
log = logging.getLogger(__name__)
log.info("I am logging for testing!!!!!!!!!!!")
################################
# from logbook import Logger, StreamHandler
# # import sys
# StreamHandler(sys.stdout).push_application()
# log = Logger(__name__)
# log.warn('This is too cool for stdlib')
################################




class AppWindow(QMainWindow):

    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)

        uic.loadUi(resource_path('pyinstaller_demo.ui'), self)

        columns_top = self.load_config('config/config.ini')

        top_values = [[1, 'Lex', 'Male', 20], [2, 'Li', 'Male', 23]]

        self.handle_ui_action()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(len(columns_top))
        self.tableWidget.setHorizontalHeaderLabels(columns_top)

        row_no = 0
        for row_value in top_values:
            column_no = 0
            for value in row_value:
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_no, column_no, item)
                column_no += 1
            row_no += 1

        columns_bottom = self.load_config('config/config2.ini')

        bottom_values = [[1, 'Lex', 96], [2, 'Li', 98]]

        self.tableWidget_2.setRowCount(3)
        self.tableWidget_2.setColumnCount(len(columns_bottom))
        self.tableWidget_2.setHorizontalHeaderLabels(columns_bottom)

        row_no = 0
        for row_value in bottom_values:
            column_no = 0
            for value in row_value:
                item = QTableWidgetItem(str(value))
                self.tableWidget_2.setItem(row_no, column_no, item)
                column_no += 1
            row_no += 1


    def handle_ui_action(self):
        pass

    def load_config(self, filepath):
        # config_file = open(resource_path('./config/config.ini'))
        config_file = open(resource_path(filepath))
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
