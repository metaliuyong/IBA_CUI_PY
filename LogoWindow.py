# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class LogoWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LogoWindow, self).__init__(parent)

        # 设置窗口大小占总屏幕大小50%
        screen = QDesktopWidget().screenGeometry()
        self.resize(screen.width() * 0.5, screen.height() * 0.5)
        # label = QLabel("hello")
        # label.setPixmap(QPixmap("../imag/icon1.ico"))
        # vbox = QVBoxLayout(self)
        # vbox.addWidget(label)
        # self.setLayout(vbox)

        # 设置LogoWindow没有边框
        self.setWindowFlags(Qt.FramelessWindowHint)

    # 用图片填充LogoWindow,这个之后可以用AI做一张这样的图
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./imag/1.jpg")
        painter.drawPixmap(self.rect(), pixmap)