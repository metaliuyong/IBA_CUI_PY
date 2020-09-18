# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from File import *
from Plot import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 设置窗口大小占总屏幕大小80%
        screen = QDesktopWidget().screenGeometry()
        self.resize(screen.width() * 0.8, screen.height() * 0.8)

        # 设置状态栏
        self.status = self.statusBar()
        self.status.showMessage("Ready")

        # 设置总标题
        self.setWindowTitle("离子束综合分析软件")

        self.fontLineEdit = QLabel("This is a font test")


        # 设置菜单栏
        menubar = self.menuBar()
        menuFile = menubar.addMenu("File")
        menuEdit = menubar.addMenu("Edit")
        menuPlot = menubar.addMenu("Plot")
        menuTools = menubar.addMenu("Tools")
        menuHelp = menubar.addMenu("Help")

        # 设置菜单栏File的Action
        actionNew = menuFile.addAction("New")
        actionOpen = menuFile.addAction(QIcon("./imag/icon1.ico"), 'Open')
        actionOpen.setShortcut("Ctrl+O")
        actionTransSpe = menuFile.addAction("Trans Spe")
        actionTransSpe.triggered.connect(self.onClickTransSpe)

        # 设置菜单栏Edit的Action
        actionCopy = menuEdit.addAction("Copy")
        actionPaste = menuEdit.addAction("Paste")

        # 设置菜单栏Plot的Action
        actionPlotSpectrum = menuPlot.addAction("Plot Spectrum")
        actionPlotSpectrum.triggered.connect(self.onClickPlotSpectrum)

        # 设置菜单栏Help的Action:Home Page,点击可以跳转到薛老师主页
        actionHomePage = menuHelp.addAction("Home Page")
        actionHomePage.triggered.connect(self.onClickHomePage)

        # 设置菜单栏Help的Action:About,点击可以弹出关于对话框
        actionAbout = menuHelp.addAction("About")
        actionAbout.triggered.connect(self.onClickAbout)

        # 设置工具栏
        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(actionOpen)

    # 定义点击HomePage的槽函数:
    def onClickHomePage(self, a):
        QDesktopServices.openUrl(QUrl('http://faculty.pku.edu.cn/~ymQJbu/zh_CN/index.htm'))

    def onClickAbout(self, a):
        information = "Author: Liu Yong\nContact: metaliuyong@gmail.com"
        QMessageBox.about(self, "About", information)

    # 定义点击TransSpe的槽函数，功能是选取一个存放Spe文件的文件夹，将其下的Spe文件全部转换为txt文件
    def onClickTransSpe(self, a):
        directory = QFileDialog.getExistingDirectory(self, "Open a folder", "../")
        print(directory)
        spe_name_list = getSpeFileNameList(directory)
        convertSpeToTxt_batch(spe_name_list)

    # 定义点击PlotSpectrum的槽函数，功能是打开一个处理好的txt文件然后画出能谱图
    def onClickPlotSpectrum(self, a):
        filename, filetype = QFileDialog.getOpenFileName(self, "Open a text file", "../", "Text Files(*.txt)")
        plotSpectrum(filename)