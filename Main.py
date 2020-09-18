# -*- coding: UTF-8 -*-

import sys
import time
from MainWindow import MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from File import convertSpeToTxt, getSpeFileNameList, convertSpeToTxt_batch
from LogoWindow import LogoWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./imag/icon0.ico"))

    logoWindow = LogoWindow()
    logoWindow.show()
    QTimer.singleShot(2000, logoWindow.hide)

    win = MainWindow()
    QTimer.singleShot(2000, win.show)
    sys.exit(app.exec())
