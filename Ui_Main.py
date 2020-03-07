# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Python\python_divide_music\Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, 0, 431, 111))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 430, 330, 15))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        self.tabChoose = QtWidgets.QTabWidget(self.centralwidget)
        self.tabChoose.setGeometry(QtCore.QRect(10, 110, 381, 311))
        self.tabChoose.setObjectName("tabChoose")
        self.tabSong = QtWidgets.QWidget()
        self.tabSong.setObjectName("tabSong")
        self.informationOfSong = QtWidgets.QTextBrowser(self.tabSong)
        self.informationOfSong.setGeometry(QtCore.QRect(10, 100, 360, 160))
        self.informationOfSong.setObjectName("informationOfSong")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tabSong)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 0, 301, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.musicLinkOfSong = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.musicLinkOfSong.setObjectName("musicLinkOfSong")
        self.gridLayout.addWidget(self.musicLinkOfSong, 0, 1, 1, 1)
        self.saveFolderOfSong = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.saveFolderOfSong.setText(os.getcwd())
        self.saveFolderOfSong.setObjectName("saveFolderOfSong")
        self.gridLayout.addWidget(self.saveFolderOfSong, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabChoose.addTab(self.tabSong, "")
        self.tabList = QtWidgets.QWidget()
        self.tabList.setObjectName("tabList")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tabList)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 0, 301, 91))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.musicLinkOfSongList = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.musicLinkOfSongList.setObjectName("musicLinkOfSongList")
        self.gridLayout_2.addWidget(self.musicLinkOfSongList, 0, 1, 1, 1)
        self.saveFolderOfSongList = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.saveFolderOfSongList.setText(os.getcwd())
        self.saveFolderOfSongList.setObjectName("saveFolderOfSongList")
        self.gridLayout_2.addWidget(self.saveFolderOfSongList, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.informationOfSongList = QtWidgets.QTextBrowser(self.tabList)
        self.informationOfSongList.setGeometry(QtCore.QRect(10, 100, 360, 160))
        self.informationOfSongList.setObjectName("informationOfSongList")
        self.tabChoose.addTab(self.tabList, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 450, 371, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.download = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.download.setObjectName("download")
        self.horizontalLayout.addWidget(self.download)
        self.cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabChoose.setCurrentIndex(0)
        self.download.clicked.connect(MainWindow.downloadClick)
        self.cancel.clicked.connect(MainWindow.exit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网易云音乐下载器"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">作者：灵道长生</p><p align=\"center\">日期：2020-1-27</p><p align=\"center\">版本：v3</p><p align=\"center\">注意：本软件无法下载“试听曲库”</p></body></html>"))
        self.informationOfSong.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Information</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "SaveFolder:"))
        self.label_2.setText(_translate("MainWindow", "MusicLink:"))
        self.tabChoose.setTabText(self.tabChoose.indexOf(self.tabSong), _translate("MainWindow", "歌曲"))
        self.label_4.setText(_translate("MainWindow", "SaveFolder:"))
        self.label_5.setText(_translate("MainWindow", "MusicLink:"))
        self.informationOfSongList.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Information</span></p></body></html>"))
        self.tabChoose.setTabText(self.tabChoose.indexOf(self.tabList), _translate("MainWindow", "歌单"))
        self.download.setText(_translate("MainWindow", "下载"))
        self.cancel.setText(_translate("MainWindow", "退出"))
