# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextFileSend.ui'
#
# Created: Mon Oct 28 01:00:05 2013
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import socket

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(587, 296)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 550, 234))
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.editIp = QtWidgets.QLineEdit(self.widget)
        self.editIp.setObjectName("editIp")
        self.verticalLayout_2.addWidget(self.editIp)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.editPort = QtWidgets.QLineEdit(self.widget)
        self.editPort.setObjectName("editPort")
        self.verticalLayout_3.addWidget(self.editPort)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.btnConnect = QtWidgets.QPushButton(self.widget)
        self.btnConnect.setObjectName("btnConnect")
        self.verticalLayout_4.addWidget(self.btnConnect)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.editTrans = QtWidgets.QLineEdit(self.widget)
        self.editTrans.setObjectName("editTrans")
        self.horizontalLayout.addWidget(self.editTrans)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.editUser = QtWidgets.QLineEdit(self.widget)
        self.editUser.setObjectName("editUser")
        self.horizontalLayout_2.addWidget(self.editUser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editPath = QtWidgets.QLineEdit(self.widget)
        self.editPath.setObjectName("editPath")
        self.horizontalLayout_3.addWidget(self.editPath)
        self.btnBrowser = QtWidgets.QPushButton(self.widget)
        self.btnBrowser.setObjectName("btnBrowser")
        self.horizontalLayout_3.addWidget(self.btnBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.btnSend = QtWidgets.QPushButton(self.widget)
        self.btnSend.setObjectName("btnSend")
        self.verticalLayout.addWidget(self.btnSend)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        self.btnBrowser.clicked.connect(self.browser)
        self.btnConnect.clicked.connect(self.ConnectServer)
        self.btnSend.clicked.connect(self.DataSend)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #add by zzhiyuan 2013年10月28日, AM 01:01:26
        self.editIp.setText('192.168.2.110')
        self.editPort.setText('10888')
        Form.setFixedSize(587, 296)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "直接对接——报文上报测试用程序"))
        self.label.setText(_translate("Form", "IP地址："))
        self.label_2.setText(_translate("Form", "端口号："))
        self.btnConnect.setText(_translate("Form", "测试连接"))
        self.label_4.setText(_translate("Form", "交易类型："))
        self.label_5.setText(_translate("Form", "柜员号："))
        self.btnBrowser.setText(_translate("Form", "浏览"))
        self.btnSend.setText(_translate("Form", "发送"))
        self.label_3.setText(_translate("Form", "反馈："))

    #选择要发送的txt文件
    def browser(self):
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(self.widget, ("打开文件"), \
                                                              "C:\\Users\\Administrator\\Desktop\\测试数据-20121014", \
                                                              ("文本文档 (*.txt)"))
        self.editPath.setText(self.fileName[0])

    #连接到服务器
    def ConnectServer(self):
        global sock
        ip = self.editIp.text()
        port = self.editPort.text()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, int(port)))
        except socket.error:
            self.textBrowser.setText('tcp连接失败.')
        else:
            self.textBrowser.setText('tcp连接成功.')

    #发送数据
    def DataSend(self):
        self.ConnectServer()
        if self.editPath.text() != '':
            fp = open(self.editPath.text())
            txtContent = fp.read()
            fp.close()
            if len(self.editTrans.text()) <= 4 and len(self.editUser.text()) <= 12:
                tmp = self.editTrans.text().rjust(4).encode('gbk') + self.editUser.text().rjust(12).encode('gbk')\
                    + b'0001' + txtContent.encode('gbk')
                strLen = str(len(tmp)).zfill(10)
                dataToSend = strLen.encode('gbk') + tmp
                try:
                    sent = sock.send(dataToSend)
                    countToRead = sock.recv(10)
                    buf = sock.recv(int(countToRead))
                    s = '发送文件:\n[' + self.editPath.text() + ']...\n\n' + '反馈：\n[' + buf.decode() + ']...'
                    self.textBrowser.setText(s)
                except OSError:
                    self.textBrowser.setText('传送失败，检查网络连接...')
            else:
                self.textBrowser.setText('交易码不能超过4位，柜员号不能超过12位...')
        else:
            self.textBrowser.setText('请选择要传送的文件...')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
