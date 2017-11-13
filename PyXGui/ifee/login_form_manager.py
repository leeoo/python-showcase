__author__ = 'Lex'

from PyQt5.QtWidgets import *
from view.loginForm import Ui_Dialog
import sys


class Login(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems([(self.tr('INT')), (self.tr('UAT')), (self.tr('PROD'))])
        self.ui.usernameLineEdit.setFocus()


def main():
    app = QApplication(sys.argv)
    loginForm = Login()
    loginForm.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()