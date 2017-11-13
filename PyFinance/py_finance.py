# -*- coding: utf-8 -*-

"""
@author         Lex Li (libeely@gmail.com)
@version        0.1
@description    App to view stock/loan/bond/index information.
"""


import sys
import os.path
import logging.config
from configparser import ConfigParser
import random
from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, sin, pi


__VERSION__ = '0.1'

# 常量声明
GB18030_ENCODING = 'GB18030'
UTF_8_ENCODING = 'UTF-8'


# Special function to import external files when using PyInstaller.
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')

    print('base_path -> %s, relative_path -> %s' % (base_path, relative_path))
    full_path = os.path.join(base_path, relative_path)
    print('full_path -> %s' % full_path)
    return full_path

################################
# 参考 https://my.oschina.net/u/150309/blog/123262
# 此处载入日志配置文件会导致PyInstaller打包后程序启动一闪而过，且任何错误提示！
# if getattr(sys, 'frozen', None):
#     basedir = sys._MEIPASS
# else:
#     basedir = os.path.dirname(__file__)
#
# logging.config.fileConfig(os.path.join(basedir, 'config/logging.ini'))
# logging.config.fileConfig(resource_path('config/logging.ini'))
# log = logging.getLogger()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)-15s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=resource_path("app.log"),
                    filemode='w')
log = logging.getLogger()
################################


class AppWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)

        self.about_message_box = None
        self.row_content_dialog = None
        self.help_message_box = None

        try:
            # self.load_config()
            log.info('配置文件加载完毕')

            # 使用PyQt5的uic来加载并解析UI文件
            uic.loadUi(resource_path('py_finance.ui'), self)

            # self.adjust_layout()

            # 支持拖拽操作
            # self.setAcceptDrops(True)  # tab_open_fund_data
            # self.dragEnterEvent(True)
            # self.tab_open_fund_data.dropped.connect(self.handle_drop_action)

            self.handle_ui_action()

            # 禁用尚未开发完成的功能
            # self.disable_in_developing_functions()
        except Exception as e:
            # error_msg = '程序内部错误，请检查运行日志！'
            error_msg = '程序内部错误，请检查运行日志！errorMsg=%s' % e
            log.error(error_msg + '异常信息：%s' % e)
            self.popup_error_msg_box(error_msg)

    def load_config(self):
        log.info('加载OFD数据文件结构定义')
        # self.load_data_file_construction_definition('data_exchange_file_definition_rule.ini')
        self.load_ofd_file_definition('config/OFD_0901_20161014.ini')
        # log.info('加载OFI索引文件结构定义')
        # self.load_index_file_construction_definition('exchange_index_file_definition_rule.ini')

    # 调整UI布局中控件间距
    def adjust_layout(self):
        # self.gridLayout.setSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setHorizontalSpacing(5)

    def handle_ui_action(self):
        # TODO 将正弦函数图画在tab_daily_k选项卡上！
        self.pushButton_stock_search.clicked.connect(self.plot_daily_k)

        # TODO 导出
        # self.button_export.clicked.connect(self.export_open_fund_data)

        # self.actionAbout.triggered.connect(self.show_about_info)
        # self.actionContent.triggered.connect(self.show_help_info)

    def plot_daily_k(self):
        print('TODO')
        self.main_widget = QWidget(self)
        layout = QVBoxLayout(self.main_widget)
        dynamic_canvas = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        layout.addWidget(dynamic_canvas)
        self.main_widget.setFocus()
        self.tab_daily_k.setLayout(layout)

    def popup_error_msg_box(self, error_msg):
        error_msg_box = QMessageBox(self)
        error_msg_box.critical(self, '错误提示', error_msg)

    def show_about_info(self):
        self.about_message_box = QMessageBox()
        self.about_message_box.setModal(True)
        self.about_message_box.setText('版本: %s\r\n\r\n当前支持（拖拽打开）的文件类型列表:\r\n%s\r\n%s'
                                       '\r\n\r\nBuilt with PyCharm and PyInstaller.'
                                       '\r\nWritten with Python 3, PyQt 5 and Qt Designer.\r\n'
                                       '\r\nBy Lex Li (libeely@gmail.com).' %
                                       (__VERSION__, list(self.ofd_config_map.keys()), '货币基金T+0对账文件'))
        self.about_message_box.show()

    def show_help_info(self):
        self.help_message_box = QMessageBox()
        self.help_message_box.setModal(True)
        self.help_message_box.setText('配置文件参见config目录')
        self.help_message_box.show()

    def disable_in_developing_functions(self):
        self.button_export.setDisabled(True)
        self.checkBox_remove_blank.setDisabled(True)
        # self.lineEdit_search_monetary.setDisabled(True)
        # self.button_search_monetary.setDisabled(True)
        self.checkBox_remove_blank_monetary.setDisabled(True)
        # self.button_restore_monetary.setDisabled(True)
        self.button_export_monetary.setDisabled(True)
        self.tab_ysstech_data.setDisabled(True)

    def handle_drop_action(self):
        log.info('Drop action emit!!!!!!!')

    def dragEnterEvent(self, dragEnterEvent):
        if dragEnterEvent.mimeData().hasUrls():
            dragEnterEvent.accept()
        else:
            dragEnterEvent.ignore()

    def dropEvent(self, dropEvent):
        for url in dropEvent.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isfile(path) and path.endswith(('.txt', '.TXT')):
                log.info(path)
                self.show_open_fund_biz_data(path)


class MyMplCanvs(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # self.axes.hold(False)  # 该方法已标注为过期，替代做法是在重画subplot前调用self.axes.clear()

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvs):
    '''静态画布： 一条正弦线'''
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot = (t, s)


class MyDynamicMplCanvas(MyMplCanvs):
    '''动态画布：每秒自动更新，更换一条折线'''
    def __init__(self, *args, **kwargs):
        MyMplCanvs.__init__(self, *args, **kwargs)
        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        random_int_nums = [random.randint(0, 10) for i in range(4)]

        self.axes.clear()  # 画之前将现有的图都清掉
        self.axes.plot([0, 1, 2, 3], random_int_nums, 'r')
        self.draw()


def main():
    app = QApplication(sys.argv)
    app_window = AppWindow()
    app_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
