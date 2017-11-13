# Refer to http://blog.csdn.net/tujiaw/article/details/40463527

import sys, time
import logging
import logging.config
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Constans
TITLE_HEIGHT = 30
FRAME_BORDER = 2


class CustomFrame(QFrame):
    def __init__(self, contentWidget, title, parent=None):
        super(CustomFrame, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)

        self.isMax_ = False
        self.isPress_ = False

        # TODO
        self.contentWidget_ = contentWidget
        # self.maxPixmap_
        # self.restorePixmap_
        # self.maxButton_

        # self.startPos_
        # self.clickPos_

        logoLabel = QLabel()
        logoPixmap = self.style().standardPixmap(QStyle.SP_TitleBarMenuButton) # QPixmap
        logoLabel.setPixmap(logoPixmap)
        logoLabel.setFixedSize(16, 16)
        logoLabel.setScaledContents(True)

        # titleLabel = QLabel()
        # titleLabel.setAlignment(Qt.AlignCenter)
        # self.titleLabel = QLabel()
        #
        # titleLabel.setText(title)
        # titleFont = titleLabel.font()
        # titleFont.setBold(True)
        # titleLabel.setFont(titleFont)
        # titleLabel.setObjectName('whiteLabel')

        # TODO Align to center
        self.windowTitle_ = title
        self.titleLabel = QLabel()
        self.titleLabel.setText(self.windowTitle_)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        # titleLabel.setFixedWidth(300)
        # titleLabel.setLineWidth(500)
        self.titleLabel.setMaximumWidth(self.width())
        self.titleLabel.setMinimumWidth(500)



        self.minButton = QToolButton()
        self.minPixmap = self.style().standardPixmap(QStyle.SP_TitleBarMinButton)
        self.minButton.setIcon(QIcon(self.minPixmap))
        self.minButton.clicked.connect(self.slotShowSmall)

        self.maxButton_ = QToolButton()
        self.maxPixmap_ = self.style().standardPixmap(QStyle.SP_TitleBarMaxButton)
        self.restorePixmap_ = self.style().standardPixmap(QStyle.SP_TitleBarNormalButton)
        self.maxButton_.setIcon(QIcon(self.maxPixmap_))
        self.maxButton_.clicked.connect(self.slotShowMaxRestore)

        self.closeButton = QToolButton()
        self.closePixmap = self.style().standardPixmap(QStyle.SP_TitleBarCloseButton)
        self.closeButton.setIcon(QIcon(self.closePixmap))
        self.closeButton.clicked.connect(self.close)

        titleLayout = QHBoxLayout()
        titleLayout.addWidget(logoLabel)
        # titleLayout.addWidget(titleLabel)
        titleLayout.addWidget(self.titleLabel)
        titleLayout.setContentsMargins(5, 0, 0, 0)
        titleLayout.addStretch()
        titleLayout.addWidget(self.minButton, 0, Qt.AlignTop)
        titleLayout.addWidget(self.maxButton_, 0, Qt.AlignTop)
        titleLayout.addWidget(self.closeButton, 0, Qt.AlignTop)
        titleLayout.setSpacing(0)
        titleLayout.setContentsMargins(5, 0, 0, 0)

        titleWidget = QWidget()
        titleWidget.setLayout(titleLayout)
        titleWidget.installEventFilter(None) #

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(titleWidget)
        mainLayout.addWidget(self.contentWidget_)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(5, 5, 5, 5) # mainLayout.setMargin(5);
        self.setLayout(mainLayout)

    def slotShowSmall(self):
        self.showMinimized()

    def slotShowMaxRestore(self):
        if self.isMax_:
            self.showNormal()
            self.maxButton_.setIcon(QIcon(self.maxPixmap_))

            # TODO
            print("After normal, Window width: " + str(self.width()))
            self.titleLabel.setFixedWidth(self.width())
        else:
            self.showMaximized()
            self.maxButton_.setIcon(QIcon(self.restorePixmap_))

            # TODO Align to center
            self.titleLabel.setAlignment(Qt.AlignCenter)
            print("After max, Window width: " + str(self.width()))
            self.titleLabel.setFixedWidth(self.width() - 30 * 3 - 3 * 3)
            self.titleLabel.setMaximumWidth(self.width())
            # TODO Need to set titleLabel align to top left!
            self.titleLabel.setText(self.windowTitle_)

        self.isMax_ = not self.isMax_

    def mousePressEvent(self, mouseEvent):
        self.clickPos_ = mouseEvent.pos()

        if mouseEvent.button() == Qt.LeftButton:
            if mouseEvent.type() == QEvent.MouseButtonPress:
                self.isPress_ = True
            elif mouseEvent.type() == QEvent.MouseButtonDblClick and mouseEvent.pos().y() <= TITLE_HEIGHT:
                self.slotShowMaxRestore()

    def mouseMoveEvent(self, mouseEvent):
        if self.isMax_ or not self.isPress_:
            return
        self.move(mouseEvent.globalPos() - self.clickPos_)

    def mouseReleaseEvent(self, mouseEvent):
        self.isPress_ = False

    # def nativeEvent(const QByteArray & eventType, void * message, long * result);

    def paintEvent(self, paintEvent):
        border = FRAME_BORDER
        if self.isMaximized():
            border = 0

        painter = QPainter(self)
        painterPath = QPainterPath()
        painterPath.setFillRule(Qt.WindingFill)
        painterPath.addRect(border, border, self.width() - 2 * border, self.height() - 2 * border)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillPath(painterPath, QBrush(Qt.white))
        color = QColor(200, 200, 200)
        for i in range(border):
            color.setAlpha((i + 1) * 30)
            painter.setPen(color)
            painter.drawRect(border - i, border - i, self.width() - (border - i) * 2, self.height() - (border - i * 2))
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)

        # 这里可以在资源中指定一张标题背景图片
        # painter.drawPixmap(QRect(border, border, self.width() - 2 * border, self.height() - 2 * border), QPixmap(DEFAULT_SKIN))
        painter.drawRect(QRect(border, TITLE_HEIGHT, self.width() - 2 * border, self.height() - TITLE_HEIGHT - border))

        QFrame.paintEvent(self, paintEvent) # 第一个参数必须是self才可以显示出来窗体


def main():
    app = QApplication(sys.argv)
    widget = QWidget()
    frame = CustomFrame(widget, 'CustomFrame')
    # frame.setStyleSheet('background-color: rgb(230, 230, 230);')
    frame.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

