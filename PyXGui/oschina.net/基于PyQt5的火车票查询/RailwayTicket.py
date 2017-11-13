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


class DataGetter():
    def getData(self, url):
        request = urllib.request.Request(url)
        opener = urllib.request.build_opener(chandle)
        try:
            response = opener.open(request)
            #chandle.cookiejar.save('f:/cookie.txt',True,True)
        except Exception:
            print('Error occurred when opening url!')
            raise Exception('Error occurred when opening url!')

        data = response.read()
        try:
            data = data.decode('utf-8')
        except:
            data = data.decode('gbk', 'ignore')
        return data

    def postData(self, url, data):
        data = urllib.parse.urlencode(data)
        data = bytes(data, 'utf-8')
        request = urllib.request.Request(url, data)
        opener = urllib.request.build_opener(chandle)
        response = opener.open(request)
        #chandle.cookiejar.save('f:/cookie.txt',True,True)
        data = response.read()
        try:
            data = data.decode('utf-8')
        except:
            data = data.decode('gbk', 'ignore')
        return data


"""火车票"""


class RailwayTicket:
    def init(self, fromStation, toStation, queryDate):
        self.li = []
        dataGetter = DataGetter()
        cont = dataGetter.getData('%s/otn/resources/js/framework/station_name.js' % RAILWAY_12306)
        fromStation = re.findall('%s\|([^|]+)' % fromStation, cont)[0]
        toStation = re.findall('%s\|([^|]+)' % toStation, cont)[0]
        url = '%s/otn/lcxxcx/query?purpose_codes=0X00&queryDate=%s&from_station=%s&to_station=%s' % (
            RAILWAY_12306, queryDate, fromStation, toStation)
        try:
            cont = json.loads(dataGetter.getData(url))["data"]["datas"]
        except Exception:
            print('Exception when getting data!')
        name = [
            "station_train_code",
            "from_station_name",
            "to_station_name",
            "lishi",
            "swz_num",
            "tz_num",
            "zy_num",
            "ze_num",
            "gr_num",
            "rw_num",
            "yw_num",
            "rz_num",
            "yz_num",
            "wz_num",
            "qt_num"
        ]
        for x in cont:
            tmp = []
            for y in name:
                if y == "from_station_name":
                    fromStation = x[y] + '\n' + x["start_time"]
                    tmp.append(fromStation)
                elif y == "to_station_name":
                    fromStation = x[y] + '\n' + x["arrive_time"]
                    tmp.append(fromStation)
                else:
                    tmp.append(x[y])
            self.li.append(tmp)


"""ui"""


class Dialog(QDialog):
    ticket = RailwayTicket()

    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.__setLayout()

        self.__createQueryBar()

        okButton = QPushButton("Ok")
        # self.layout[1].addWidget(okButton)
        okButton.clicked.connect(self.submit)

        self.__creatTableWidget()

        self.layout[1].addWidget(okButton)
        self.layout[0].addWidget(self.table)

        self.show()

    def submit(self):
        self.table.clearContents()
        fromStation = self.queryBar[0].text()
        toStation = self.queryBar[1].text()
        queryDate = self.queryBar[2].currentText()
        self.ticket.init(fromStation, toStation, queryDate)
        self.table.setRowCount(len(self.ticket.li))

        i = 0
        for x in self.ticket.li:
            j = 0
            for y in x:
                if j == 1 or j == 2:
                    item = QLabel(y)
                    item.setAlignment(Qt.AlignCenter)
                    self.table.setCellWidget(i, j, item)
                else:
                    item = QTableWidgetItem(y)
                    item.setTextAlignment(Qt.AlignCenter)
                    if not re.search('\D', y):
                        item.setForeground(QBrush(Qt.red))
                    self.table.setItem(i, j, item)
                if j > 2 or j == 0:
                    self.table.resizeColumnToContents(j)
                j += 1
            i += 1

    def __setLayout(self):
        #布局管理器
        self.layout = [QVBoxLayout(self), QHBoxLayout()]
        self.layout[1].setContentsMargins(0, 0, 0, 0)
        self.layout[1].setSpacing(0)
        self.layout[0].setContentsMargins(0, 0, 0, 0)
        self.layout[0].setSpacing(0)
        self.layout[0].addLayout(self.layout[1])

    def __creatTableWidget(self):
        #表格
        # TODO
        head = ['车次', '发站', '到站', '历时', '商务座', '特等座', '一等座', '二等座', '高级软卧', '软卧', '硬卧', '软座', '硬座', '无座', '其他']
        self.table = QTableWidget()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setColumnCount(len(head))
        self.table.setHorizontalHeaderLabels(head)

    def __createQueryBar(self):
        #输入选项
        queryBarLabels = [QLabel("发站："), QLabel("到站："), QLabel("日期：")]
        self.queryBar = [QLineEdit(), QLineEdit(), QComboBox()]
        year = int(time.strftime("%Y", time.localtime()))
        month = int(time.strftime("%m", time.localtime()))
        day = int(time.strftime("%d", time.localtime()))
        print('%s, %s, %s' % (year, month, day))
        dateListSize = 20
        dateList = self.constructQueryDateList(year, month, day, dateListSize)
        # print('dateList -> %s' % dateList)
        self.queryBar[2].addItems(dateList)
        i = 0
        while i < len(self.queryBar):
            self.queryBar[i].setMaximumWidth(100)
            queryBarLabels[i].setMaximumWidth(50)
            queryBarLabels[i].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.layout[1].addWidget(queryBarLabels[i], Qt.AlignRight)
            self.layout[1].addWidget(self.queryBar[i], Qt.AlignLeft)
            i += 1

    def constructQueryDateList(self, year, month, day, dateListSize):
        i = 0
        yy = year
        mm = month
        dd = day
        dateList = []
        while i < dateListSize:
            if month in (1, 3, 5, 7, 8, 10, 12):
                if day + i > 31:
                    dd = day + i - 31
                    mm = month + 1
                    if mm > 12:
                        yy = year + 1
                        mm = mm - 12
                else:
                    dd = day + i
            elif month in (4, 6, 9, 11):
                if day + i > 30:
                    dd = day + i - 30
                    mm = month + 1
                    if mm > 12:
                        yy = year + 1
                        mm = mm - 12
                else:
                    dd = day + i
            else:
                if (month % 400 == 0) or ((month % 4 == 0) and (month % 100 != 0)):
                    if day + i > 29:
                        dd = day + i - 29
                        mm = month + 1
                        if mm > 12:
                            yy = year + 1
                            mm = mm - 12
                    else:
                        dd = day + i
                else:
                    if day + i > 28:
                        dd = day + i - 28
                        mm = month + 1
                        if mm > 12:
                            yy = year + 1
                            mm = mm - 12
                    else:
                        dd = day + i
            dateList.append('%d-%02d-%02d' % (yy, mm, dd))
            i += 1
        return dateList


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(app.exec())