#!/bin/python
# -*- coding: utf-8 -*-
################################################################################
# author: Lex Li
# version: 1.0
################################################################################


import sys
import time
import logging
import logging.config
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from view.dashboard import Ui_dashboardTabWidget
from view.login_form import Ui_loginFormDialog
from view.account_edit_form import Ui_AccountEditFormDialog
from account.user_dao import UserDao
from account.account_dao import AccountDao
from account.account import Account
from common.log4p import logit


from account.account_service import AccountService

'''
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
# Create file handler with a higher log level
fh = logging.FileHandler('ifee.log')
fh.setLevel(logging.INFO)
# Create console handler which logs even info messages
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatr(formatter)
log.addHandler(fh)
log.addHandler(ch)
'''

################################
logging.config.fileConfig('config/logging.ini')
log = logging.getLogger()
################################
# Constants
# CASCADE_SEPERATOR = ' // '
# CASCADE_SEPERATOR = ' » '
# CASCADE_SEPERATOR = ' 〉'
CASCADE_SEPERATOR = ' ＞ '  # Looks better on title bar.
# CASCADE_SEPERATOR = ' ＜ '
# CASCADE_SEPERATOR = ' > '
# CASCADE_SEPERATOR = ' >>> '
# CASCADE_SEPERATOR = ' 》'
# CASCADE_SEPERATOR = ' ) '
# CASCADE_SEPERATOR = ' )) '
# CASCADE_SEPERATOR = ' } '
# CASCADE_SEPERATOR = ' }} '
# CASCADE_SEPERATOR = '｜'
# CASCADE_SEPERATOR = '↑↓←→↖↗↙↘'
# CASCADE_SEPERATOR = ' ⇨ '
# CASCADE_SEPERATOR = ' ▷ '


def apply_external_style():
    # TODO Apply external Qt Style Sheet
    style_file = QFile('theme/metro.qss')
    style_file.open(QFile.ReadOnly)
    style_sheet = style_file.readAll()
    style_sheet = str(style_sheet, encoding='utf-8')
    qApp.setStyleSheet(style_sheet)


class MainForm(QTabWidget):
    # 类级别的成员变量，使用类名加点的方式来调用
    account_service = AccountService()
    log.debug(account_service)

    def __init__(self, parent=None):
        # QWidget.__init__(self, parent)
        super(MainForm, self).__init__(parent)

        # 设置无边框窗体，这会导致该窗体无法改变大小或移动
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.windowTitleBar = QStyleOptionTitleBar()

        self.ui = Ui_dashboardTabWidget()
        self.ui.setupUi(self)

        apply_external_style()

        self.head_4_account_tab = ['#', 'User Name', 'Gender', 'Age', 'Tel No.', 'E-mail', 'Description',
                                   'Creator', 'Modifier', 'Creation Time', 'Modification Time',
                                   'Account Enabled', 'Account Locked', 'Account Expired', 'Credentials Expired']

        # TODO 连接"用户"选项卡的按钮的信号与槽
        self.ui.refreshButton.clicked.connect(self.refresh)
        self.ui.newButton.clicked.connect(self.to_new_account_form)
        self.ui.searchButton.clicked.connect(self.search_account_list)
        self.ui.importButton.clicked.connect(self.to_import_account_form)
        self.ui.updateButton.clicked.connect(self.to_edit_account_form)
        self.ui.deleteButton.clicked.connect(self.delete_account_and_update_account_form)
        self.ui.refresh.clicked.connect(self.refresh)
        self.ui.createRow.clicked.connect(self.to_new_account_form)
        self.ui.editRow.clicked.connect(self.to_edit_account_form)
        self.ui.deleteRow.clicked.connect(self.delete_account_and_update_account_form)

        # self.ui.accountTabWidget.currentChanged['int'].connect(self.updateMainWindowTitle)
        # TODO 当切换选项卡后更新主窗体标题
        # self.currentChanged['int'].connect(self.updateMainWindowTitle)
        # <=>
        self.tabBarClicked['int'].connect(self.update_main_window_title)

        self.tabBarDoubleClicked['int'].connect(self.close_tab)

        # 为了显示美观，调整accountManageTab的queryBar
        labels_in_account_manage_tab_query_bar = [self.ui.useridLabel, self.ui.usernameLabel, self.ui.emailLabel,
                                                  self.ui.phoneNoLabel, self.ui.registYearLabel]
        line_edits_in_account_manage_tab_query_bar = [self.ui.useridLineEdit, self.ui.usernameLineEdit,
                                                      self.ui.emailLineEdit, self.ui.phoneNoLineEdit]
        for label in labels_in_account_manage_tab_query_bar:
            label.setMaximumWidth(70)
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        for lineEdit in line_edits_in_account_manage_tab_query_bar:
            lineEdit.setMaximumWidth(180)

        current_year = int(time.strftime('%Y', time.localtime()))
        # 为了查找最近5年内注册的账户，使用lambda表达式生成近5年的年份数据列表
        regist_years = [str((current_year - i)) for i in range(5)]
        self.ui.registYearComboBox.addItems(regist_years)

        # TODO Load account list from DB.
        # account_list = MainForm.account_service.list()
        account_list = MainForm.account_service.list_4_account_manage_tab()
        # account_list = self.loadAccountList()

        self.build_account_table_view(self.head_4_account_tab, account_list)

    # TODO Override paintEven method to re-paint.
    """
    def paintEvent(self, QPaintEvent):
        painter = QStylePainter(self);
        # painter.drawPrimitive(QStyle.CC_TitleBar, option)
        option = QStyleOptionTitleBar()
        option.initFrom(self)
        painter.drawControl(QStyle.CC_TitleBar, option)


        painter.begin(self);
        log.info('-------------------window title---> ' + self.windowTitle())
        # Your drawing code goes here.
        # self.setWindowTitle('TESt for re-paint!')
        # self.initStyleOption(option, 1)
        # painter.drawControl(QStyleOptionTitleBar, option)
        # painter.drawText(self.window(), Qt.AlignCenter, self.windowTitle())
        # painter
        # windowTitle = self.windowTitle()
        # windowTitle.center(100, 'just for center align test')
        # painter.drawControl()
        # painter.drawText(self.windowTitle, Qt.AlignCenter)
        # painter.draw
        painter.end();
"""

    def build_account_table_view(self, head, account_list):
        log.debug('header -> %s' % head)
        log.debug('account_list -> %s' % str(account_list))

        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setColumnCount(len(head))
        self.ui.tableWidget.setHorizontalHeaderLabels(head)
        # 必须同时设置rowCount和columnCount才能让表格显示！
        self.ui.tableWidget.setRowCount(len(account_list))
        i = 0
        for account in account_list:
            j = 0
            for cell in account:
                if cell is None:
                    cell = ''
                # Cell与Item的区别参见 http://www.qtcn.org/bbs/read-htm-tid-23603.html
                # item = QLabel(str(cell))
                # item.setAlignment(Qt.AlignCenter)
                # self.ui.tableWidget.setCellWidget(i, j, item)

                table_widget_item = QTableWidgetItem(str(cell))
                table_widget_item.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget.setItem(i, j, table_widget_item)
                j += 1
            i += 1

            # i = 0
            # for account in account_list:
            #     accountDict = account.toString()
            #     if cell is None:
            #         cell = ''
            #     account.
            #     item = QLabel(str(cell))
            #     item.setAlignment(Qt.AlignCenter)
            #     self.ui.tableWidget.setCellWidget(i, j, item)
            #     i += 1

    def close_tab(self, index):
        self.widget(index).close()

    def update_main_window_title(self, tab_id):
        print('tab_id -> %d, tabCount -> %d' % (tab_id, self.ui.accountTabWidget.count()))
        print(self.ui.accountTabWidget.widget(tab_id))
        # self.ui.accountTabWidget.widget(tab_id).setWindowTitle('个人数据管理 - ' + str(tab_id))

        temp_widget = QWidget()
        temp_button = QPushButton('click me!')
        temp_layout = QHBoxLayout(temp_widget)
        temp_layout.addWidget(temp_button)
        temp_widget.setLayout(temp_layout)

        # self.ui.accountTabWidget.addTab(temp_widget, 'tab_' + str(tab_id))
        log.debug(self.windowTitle())
        log.debug(type(self))
        # self.ui.accountTabWidget.setTabText(tab_id, '111111111')
        # self.setWindowTitle('个人数据管理 - ' + self.tabText(tab_id))
        self.setWindowTitle('个人数据管理' + CASCADE_SEPERATOR + self.tabText(tab_id))

        log.debug(type(self.widget(tab_id)))
        wdgt = self.widget(tab_id)
        # wdgt = self.children()[tab_id]
        # wdgt = self.widget(tab_id).parent()
        log.debug(type(wdgt))
        # log.debug(wdgt.tabText())

        # self.setWindowTitle('个人数据管理 - ' + self.tabText(tab_id) + '_tab' + str(tab_id))
        # self.setWindowTitle('个人数据管理 - ' + self.ui.accountTabWidget.tabText(tab_id) + '_tab' + str(tab_id))

    def init_account_manage_tab(self):
        # account_list = MainForm.account_service.list()
        account_list = self.account_service.list
        log.debug(account_list)
        log.info("account_list size -> %d" % len(account_list))
        return account_list

    # TODO Dispatch action here ?
    def handle_action(self):
        log.debug('test...............')
        pass

    def refresh(self):
        # Load account list from DB.
        # account_list = MainForm.account_service.list()
        # account_list = MainForm.account_service.list4AccountManageTab()
        # account_list = MainForm.account_service.list4AccountTabByUsername('user')
        account_list = MainForm.account_service.list_all()
        log.debug(account_list)
        # account_list = self.loadAccountList()

        log.info('Refreshing account table view...')
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.show()
        self.build_account_table_view(self.head_4_account_tab, account_list)
        log.info('Refresh account table view successfully!')

    def search_account_list(self):
        account_id_text = self.ui.useridLineEdit.text()
        account_id = -1
        try:
            account_id = int(account_id_text)
        except ValueError as ve:
            # TODO
            log.error('Invalid integer number!', ve)

        username = self.ui.usernameLineEdit.text()
        email = self.ui.emailLineEdit.text()
        phone_no = self.ui.phoneNoLineEdit.text()
        regist_year = self.ui.registYearComboBox.currentText()
        search_criteria_dict = {
            'accountId': account_id,
            'username': username,
            'email': email,
            'phoneNo': phone_no,
            'registYear': regist_year + '-12-31'  # ie.g. 2014-12-31
        }
        log.info('Searching account list with parameters %s ...' % search_criteria_dict)
        account_list = MainForm.account_service.list(search_criteria_dict)
        log.info('account_list -> %s' % account_list)
        self.build_account_table_view(self.head_4_account_tab, account_list)

    '''
    1) Check if there is one of items is selected.
    2) Get ids from selected items.
    3) Delete data from DB by ids.
    4) Update table widget.
     '''
    def delete_account_and_update_account_form(self):
        accounts = None
        # log.info(self.ui.tableWidget.SelectRows())

        # 0) Get selected row indexes
        row_indexes = self.get_selected_row_indexes()
        log.debug('Selected rows -> %s' % row_indexes)

        # 1) Check if there is one of items is selected.
        if len(row_indexes) == 0:
            log.warn('No row selected, do nothing!')
            return

        # 2) Get ids from selected items.
        account_ids = self.__get_account_ids()

        # 3) Delete data from DB by ids.
        for account_id in account_ids:
            MainForm.account_service.delete_by_id(account_id)

        log.debug("Table's column count: %s" % self.ui.tableWidget.columnCount())
        log.debug("Table's row count: %s" % self.ui.tableWidget.rowCount())
        log.debug(self.ui.tableWidget.selectedItems())
        # for idx in self.ui.tableWidget.selectedItems():
        #     print(idx)

        # 4) Update table widget.
        for row_index in row_indexes:
            self.ui.tableWidget.removeRow(row_index)

    def get_selected_row_indexes(self):
        selected_cell_indexes = self.ui.tableWidget.selectedIndexes()
        row_indexes = []  # row indices
        for coordinate in selected_cell_indexes:
            row_index = coordinate.row()
            row_indexes.append(row_index)
        row_indexes = list(set(row_indexes))
        row_indexes.sort(reverse=True)  # Sort row indexes by reverse to avoid table widget update issue!
        return row_indexes

    def __get_account_ids(self):
        rows = []
        account_ids = []
        usernames = []
        selected_cell_indexes = self.ui.tableWidget.selectedIndexes()
        for idx in selected_cell_indexes:
            log.debug(idx.row)
            log.debug(idx.row())
            log.debug(idx.column)
            log.debug(idx.column())
            rows.append(idx.row)
            # account_id = int(self.ui.tableWidget.cellWidget(idx.row(), 0).text())  # 单元格是CellWidget的情形
            account_id = int(self.ui.tableWidget.item(idx.row(), 0).text())
            log.debug(account_id)
            account_ids.append(account_id)
            # username = self.ui.tableWidget.cellWidget(idx.row(), 1).text()
            username = self.ui.tableWidget.item(idx.row(), 1).text()
            log.debug(username)
            usernames.append(username)
        # log.debug(rows[0].items)
        account_ids = list(set(account_ids))
        log.debug(type(account_ids))
        usernames = list(set(usernames))
        log.debug('Account ids -> %s' % str(account_ids))
        log.debug('Account user names -> %s' % str(usernames))
        return account_ids

    def to_import_account_form(self):
        _filename = QFileDialog.getOpenFileName(self.ui.accountTab, ('打开文件'), \
                                                'C:/Users/leeoo/桌面', ('CSV文件 (*.csv); TXT文件 (*.txt)'))
        log.info('filename -> %s' % str(_filename))
        # TODO

    # TODO 新建后要重新load数据
    def to_new_account_form(self):
        log.debug('In to_new_account_form method!')
        # 此处创建AccountEditForm窗体对象时需要传入self对象，否则创建的窗体不受创建它的主窗体控制
        account_edit_form = AccountEditForm(self)
        # 设置窗体为模态
        account_edit_form.setModal(True)
        account_edit_form.show()

        account_edit_form.ui.accountIdLineEdit.setReadOnly(True)

    # TODO 新建后要重新load数据
    def to_edit_account_form(self):
        log.debug('In to_edit_account_form method!')
        row_indexes = self.get_selected_row_indexes()
        if len(row_indexes) != 1:
            log.warn('Must select only one row!')
            return

        # TODO
        selected_row = row_indexes[0]
        # current_row = self.ui.accountTab.selectRow(selected_row)
        # log.debug(type(current_row))
        row_values = []
        column_count = self.ui.tableWidget.columnCount()
        for i in range(column_count):
            column_value = self.ui.tableWidget.item(selected_row, i).text()
            row_values.append(column_value)
        log.debug("selected row's column values: %s" % row_values)

        # 此处创建AccountEditForm窗体对象时需要传入self对象，否则创建的窗体不受创建它的主窗体控制
        account_edit_form = AccountEditForm(self)
        # 设置窗体为模态
        account_edit_form.setModal(True)
        account_edit_form.show()

        # TODO 填充选中行的数据到account_edit_form
        account_edit_form.ui.accountIdLineEdit.setText(row_values[0])
        account_edit_form.ui.accountIdLineEdit.setReadOnly(True)
        account_edit_form.ui.userNameLineEdit.setText(row_values[1])
        account_edit_form.ui.userNameLineEdit.setReadOnly(True)

        # account_edit_form.ui.passwordLineEdit.setText(row_values[2])
        # account_edit_form.ui.passwordAgainLineEdit.setText(row_values[2])
        # account_edit_form.ui.passwordHintLineEdit.setText(row_values[3])
        gender = row_values[2]
        if gender == 'Male'.lower():
            account_edit_form.ui.radioButton.setChecked(True)
        elif gender == 'Female'.lower():
            account_edit_form.ui.radioButton_2.setChecked(True)
        else:
            log.info('No gender checked!')

        account_edit_form.ui.ageLineEdit.setText(row_values[3])
        account_edit_form.ui.telNoLineEdit.setText(row_values[4])
        account_edit_form.ui.emailLineEdit.setText(row_values[5])
        account_edit_form.ui.descriptionLineEdit.setText(row_values[6])
        # account_edit_form.ui.userGroupComboBox.setCurrentText(row_values[7])
        # account_edit_form.ui.roleComboBox.setCurrentText(row_values[8])

        account_edit_form.ui.accountEnabledCheckBox.setChecked(row_values[11] == 'True')
        account_edit_form.ui.accountLockedCheckBox.setChecked(row_values[12] == 'True')
        account_edit_form.ui.accountExpiredCheckBox.setChecked(row_values[13] == 'True')
        account_edit_form.ui.credentialsExpiredCheckBox.setChecked(row_values[14] == 'True')

        # account_edit_form.ui.creatorLineEdit.setText()
        account_edit_form.ui.creatorLineEdit.setReadOnly(True)
        account_edit_form.ui.modifierLineEdit.setText('ifee')
        account_edit_form.ui.modifierLineEdit.setReadOnly(True)
        # account_edit_form.ui.modificationTimeLineEdit.setText()
        account_edit_form.ui.modificationTimeLineEdit.setReadOnly(True)


class LoginForm(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_loginFormDialog()
        self.ui.setupUi(self)

        apply_external_style()

        # Set combo box items.
        item_list = [self.tr('INT'), self.tr('UAT'), self.tr('PROD')]
        self.ui.envComboBox.addItems(item_list)
        # 默认让username文本框获得焦点
        self.ui.usernameLineEdit.setFocus()

        # TODO Using default account for development/test/demo.
        env = self.ui.envComboBox.currentText()
        log.info('env -> %s' % env)
        if env is None or env.strip() == '':
            err_msg = "The env can't be empty!"
            log.error(err_msg)
            raise ValueError(err_msg)

        self.use_temp_account_4_non_prod_env(env)

        self.ui.envComboBox.currentIndexChanged['QString'].connect(self.set_default_input_4_env)

        self.ui.buttonBox.accepted.connect(self.login)
        # 这句已经被QDialog自己内部实现，见生成的loginForm.py
        # self.ui.buttonBox.rejected.connect(self.reject)

        self.user_dao = UserDao()
        self.account_dao = AccountDao()

    def use_temp_account_4_non_prod_env(self, env):
        log.debug(id(env))
        log.debug(id('PROD'))
        if env != 'PROD' or env != 'COB':
            log.info('Current env [ %s ] is not PROD/COB env, using temp account for development/demo/test!' % env)
            self.ui.usernameLineEdit.setText('ifee')
            self.ui.passwordLineEdit.setText('ifee')

    def set_default_input_4_env(self, text):
        if text == 'PROD' or text == 'COB':
            self.ui.usernameLineEdit.setText('')
            self.ui.passwordLineEdit.setText('')
        else:
            self.ui.usernameLineEdit.setText('ifee')
            self.ui.passwordLineEdit.setText('ifee')

    def login(self):
        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        # user = self.userDao.getUserByUsername(username)
        # print(self.userDao.getUserById(1))

        # account = self.account_dao.getAccountByUsername(username)

        account = None
        try:
            account = self.account_dao.get_by_name(username)
        except Exception as e:
            raise e
        log.debug(self.account_dao.get_by_id(1))
        log.debug(type(account))
        log.debug(account)

        # if self.ui.usernameLineEdit.text() == 'admin' and self.ui.passwordLineEdit.text() == '123456':
        # if user is not None and password == user[2] or 1 == 1:
        # if account is not None and username == account[1] and password == account[2] \
        #         or 1 == 1:
        if account is not None and username.strip() != '' and username == account[2] and password == account[3]:
            self.accept()
        else:
            '''
             Note: 一定记得要把loginForm.py当中的由Qt Designer默认生成的accepted信号与槽accept的连接(即下面这行)给删掉，
                否则账号密码不对也会进主界面！！！
             self.buttonBox.accepted.connect(loginFormDialog.accept)
            '''

            # QMessageBox.critical(self, '登录失败', '用户名或密码不匹配！')
            # TODO
            # self.ui.labelAlert.setStyleSheet("color: rgb(255, 0, 0);font: italic bold 9pt \"Arial\";")
            self.ui.labelAlert.setStyleSheet("color: rgb(255, 0, 0);font: bold 9pt \"Arial\";")
            #             self.ui.labelAlert.setStyleSheet("color: rgb(255, 0, 0)")
            self.ui.labelAlert.setText('登录失败,用户名或密码不匹配！')
            log.debug(self.ui.labelAlert.text())
            # time.sleep(0.5)
            # self.ui.labelAlert.setText('')


class AccountEditForm(QDialog):
    def __init__(self, parent=None):
        # QWidget.__init__(self, parent)
        # QDialog.__init__(self, parent)
        super(AccountEditForm, self).__init__(parent)
        self.ui = Ui_AccountEditFormDialog()
        self.ui.setupUi(self)

        # TODO 设置radio button组
        self.gender_group = QButtonGroup()
        self.gender_group.addButton(self.ui.radioButton, 0)
        self.gender_group.addButton(self.ui.radioButton_2, 1)

        self.accountDao = AccountDao()

        # 连接信号与槽
        self.ui.buttonBox.clicked.connect(self.save_account)

    def save_account(self):
        _accountid = self.ui.accountIdLineEdit.text()
        if _accountid is not None and _accountid != '':
            log.info('Just update a exist account')
        else:
            _accountid = None
            log.info('Just create a new account')

        _username = self.ui.userNameLineEdit.text()
        _password = self.ui.passwordLineEdit.text()
        # _passwordAgain = self.ui.passwordAgainLineEdit.text()
        # _passwordHint = self.ui.passwordHintLineEdit.text()

        checked_id = self.gender_group.checkedId()
        _gender = ''
        if checked_id == 0:
            _gender = 'male'
        elif checked_id == 1:
            _gender = 'female'
        else:
            log.warn('No gender selected!')

        _age = self.ui.ageLineEdit.text()
        _telNo = self.ui.telNoLineEdit.text()
        _email = self.ui.emailLineEdit.text()
        _description = self.ui.descriptionLineEdit.text()
        _department = self.ui.departmentComboBox.currentText()
        _userGroup = self.ui.userGroupComboBox.currentText()
        _role = self.ui.roleComboBox.currentText()
        _accountEnabled = self.ui.accountEnabledCheckBox.isChecked()
        _accountLocked = self.ui.accountLockedCheckBox.isChecked()
        _accountExpired = self.ui.accountExpiredCheckBox.isChecked()
        _credentialsExpired = self.ui.credentialsExpiredCheckBox.isChecked()
        # _passwordAgain = self.ui.
        # TODO
        # print('username: %s, password: %s, department: %s, accountEnabled: %s' % (
        #     _username, _password, _department, _accountEnabled))

        # TODO
        # log.debug('type(self)')
        # log.debug(type(self))
        # log.debug('type(self.parent())')
        # log.debug(type(self.parent()))
        # log.debug('type(self.parent().parent())')
        # log.debug(type(self.parent().parent()))

        # TODO 添加验证逻辑(需要禁用accountEditForm.py里的accepted信号槽连接)
        if _username == '' or _password == '':
            # self.setWindowTitle(self.windowTitle() + ' - Can\'t submit when nothing input!')
            self.setWindowTitle('Account Edit Form' + ' - Can\'t submit when nothing input!')
            log.warn('Can\'t submit when nothing input!')
            return

        account_ = Account()
        account_.accountId = _accountid
        account_.username = _username
        account_.password = _password
        account_.salt = 'abc123'
        account_.passwordHint = None
        account_.age = _age
        account_.gender = _gender
        account_.phoneNo = _telNo
        account_.email = _email
        account_.description = _description
        account_.creator = None
        account_.modifier = None
        # account_.createTime = _creationTime
        # account_.updateTime = _modificationTime
        account_.accountEnabled = _accountEnabled
        account_.accountLocked = _accountLocked
        account_.accountExpired = _accountExpired
        account_.credentialsExpired = _credentialsExpired

        try:
            self.accountDao.save_or_update(account_)
            self.accept()
        except Exception as e:
            # TODO
            log.error('Exception saving account!', e)


@logit
def login():
    login_form = LoginForm()
    try:
        if login_form.exec():
            log.debug('call login...')
            return True
        else:
            return False
    except Exception as e:
        raise e


def main():
    app = QApplication(sys.argv)

    try:
        if login():
            main_form = MainForm()
            main_form.handle_action()
            main_form.show()
            sys.exit(app.exec())
    except Exception as e:
        error_dialog = QDialog()
        error_dialog.show()
        msg = 'Exception logging on system!'
        log.error(msg, e)


if __name__ == '__main__':
    main()
