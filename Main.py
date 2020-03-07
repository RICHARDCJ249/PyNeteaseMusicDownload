#coding = utf-8

import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from Ui_Main import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import downloadNeteaseMusiclib
import queue
import re

musicLink = queue.Queue(maxsize=20)
saveFolder = queue.Queue(maxsize=20)


class DownloadMusicWindow(QMainWindow):

    INFO = 0
    ERROR = 1
    DEBUG = 2

    def __init__(self, Ui_MainWindow):
        self.bufferString = []
        self.debug = True
        self.ui = Ui_MainWindow
        super().__init__()

    def print_(self, type, s):
        if self.bufferString.__len__() >= 9:
            self.bufferString.clear()
        if type == self.INFO:
            self.bufferString.append('<b>Info:</b> <span style="color: #00FF00">{}.</span>'.format(s))
        elif type == self.ERROR:
            self.bufferString.append('<b>Error:</b> <span style="color:#ff0000">{}</span>.'.format(s))
        elif type == self.DEBUG and self.debug == True:
            self.bufferString.append('<b>DEBUG:</b> {}.'.format(s))
        if self.ui.tabChoose.currentIndex() == 0:
            self.ui.informationOfSong.setText('<br>'.join(self.bufferString))
        else:
            self.ui.informationOfSongList.setText('<br>'.join(self.bufferString))

    def update_(self,type,s):
        if self.bufferString.__len__() >= 9:
            self.bufferString.clear()
        self.bufferString.pop()
        if type == self.INFO:
            self.bufferString.append('<b>Info:</b> <span style="color: #00FF00">{}</span>.'.format(s))
        elif type == self.ERROR:
            self.bufferString.append('<b>Error:</b> {}.'.format(s))
        elif type == self.DEBUG and self.debug == True:
            self.bufferString.append('<b>DEBUG:</b> {}.'.format(s))
        if self.ui.tabChoose.currentIndex() == 0:
            self.ui.informationOfSong.setText('<br>'.join(self.bufferString))
        else:
            self.ui.informationOfSongList.setText('<br>'.join(self.bufferString))

    def clear_(self):
        self.bufferString.clear()
        if self.ui.tabChoose.currentIndex() == 0:
            self.ui.informationOfSong.setText('<br>'.join(self.bufferString))
        else:
            self.ui.informationOfSongList.setText('<br>'.join(self.bufferString))

    def exit(self):
        sys.exit(0)

    def updata(self,precient,s):
        self.ui.progressBar.setValue(precient)
        if s.find('speed') == -1:
            self.print_(self.INFO,s)
        else:
            self.update_(self.INFO,s)

    def error(self,s):
        self.print_(self.ERROR,s)

    def downloadClick(self):
        global musicLink
        global saveFolder

        self.ui.progressBar.setVisible(True)
        self.ui.progressBar.setValue(1)
        self.ui.informationOfSong.setFontPointSize(10)
        if self.ui.tabChoose.currentIndex() == 0:
            if self.ui.musicLinkOfSong.text() != '' and self.ui.saveFolderOfSong.text() != '':
                self.print_(
                    self.INFO, 'MusicLink > {}'.format(self.ui.musicLinkOfSong.text()))
                self.print_(
                    self.INFO, 'SaveFolder > {}'.format(self.ui.saveFolderOfSong.text()))
                self.clear_()
                if not (os.path.exists(self.ui.saveFolderOfSong.text())):
                    os.mkdir(self.ui.saveFolderOfSong.text())
                musicLink.put(self.ui.musicLinkOfSong.text())
                saveFolder.put(self.ui.saveFolderOfSong.text())
                self.print_(self.INFO, '开始下载线程')
                self.Thread = downloadNeteaseMusicOneThread()
                self.Thread.signUpData.connect(self.updata)
                self.Thread.singError.connect(self.error)
                self.Thread.signClear.connect(self.clear_)
                self.Thread.start()
            else:
                self.error('请查看是否填写MusicLink或者SaveFolder')

        elif self.ui.tabChoose.currentIndex() == 1:

            if self.ui.musicLinkOfSongList.text() != '' and self.ui.saveFolderOfSongList.text() != '':
                self.print_(
                    self.INFO, 'MusicLink > {}'.format(self.ui.musicLinkOfSongList.text()))
                self.print_(
                    self.INFO, 'SaveFolder > {}'.format(self.ui.saveFolderOfSongList.text()))
                self.clear_()
                if not (os.path.exists(self.ui.saveFolderOfSongList.text())):
                    os.mkdir(self.ui.saveFolderOfSongList.text())
                musicLink.put(self.ui.musicLinkOfSongList.text())
                saveFolder.put(self.ui.saveFolderOfSongList.text())
                self.print_(self.INFO, '开始下载线程')
                self.Thread = downloadNeteaseMusicListThread()
                self.Thread.signUpData.connect(self.updata)
                self.Thread.singError.connect(self.error)
                self.Thread.signClear.connect(self.clear_)
                self.Thread.start()
            else:
                self.error('请查看是否填写MusicLink或者SaveFolder')


class downloadNeteaseMusicOneThread(QtCore.QThread):

    signUpData = QtCore.pyqtSignal(int, str)
    singError = QtCore.pyqtSignal(str)
    signClear = QtCore.pyqtSignal()

    def fetch_song_list(self, id) -> list:
        return downloadNeteaseMusiclib.fetch_song_list(id)

    def download_music_by_id(self, saveFolder, information, updateFun) -> bool:
        return downloadNeteaseMusiclib.download_music_by_id(
            saveFolder, information, updateFun)

    def getInformationByID(self, id) -> dict:
        return downloadNeteaseMusiclib.getInformationByID(id)

    def fillInformation(self, saveFolder, information) -> bool:
        return downloadNeteaseMusiclib.fillInformation(saveFolder, information)

    def updateFun(self, length, t):
        self.signUpData.emit(3+int((t/length)*80),
                             'speed -> {} byte - {} byte'.format(t, length))

    def run(self):
        global saveFolder
        global musicLink

        _saveFloder = saveFolder.get()
        _musicLink = musicLink.get()
        if _saveFloder != '' and _musicLink != '':
            _id = re.findall(r'song\?id=(\d+)', _musicLink)[0]
            self.signUpData.emit(3, '成功获取id')
            information = self.getInformationByID(_id)
            self.signUpData.emit(9, '{}||{}||{}'.format(
                information['name'], information['author'], information['album']))
            self.signUpData.emit(10,'')
            self.download_music_by_id(
                _saveFloder, information, self.updateFun)
            self.signUpData.emit(80, '下载成功')
            self.fillInformation(_saveFloder, information)
            self.signUpData.emit(100, '写入Tag成功')
            self.quit()


class downloadNeteaseMusicListThread(downloadNeteaseMusicOneThread):

    def run(self):
        _saveFloder = saveFolder.get()
        _musicLink = musicLink.get()
        if _saveFloder != '' and _musicLink != '':
            _id = re.findall(r'playlist\?id=(\d+)', _musicLink)[0]
            self.signUpData.emit(3, '成功获取歌单id')
            songName, songIdList = self.fetch_song_list(_id)
            if not os.path.exists(os.path.join(_saveFloder,songName)):
                os.mkdir(os.path.join(_saveFloder,songName))
                _saveFloder = os.path.join(_saveFloder,songName)
            for _ in songIdList:
                try:
                    self.signClear.emit()
                    self.signUpData.emit(7,'{}'.format(songName))
                    self.signUpData.emit(8,'{} in {}'.format(songIdList.index(_)+1,songIdList.__len__())) 
                    information = self.getInformationByID(_)
                    self.signUpData.emit(9, '{}||{}||{}'.format(
                        information['name'], information['author'], information['album']))
                    self.signUpData.emit(10,'')
                    self.download_music_by_id(
                        _saveFloder, information, self.updateFun)
                    self.signUpData.emit(80, '下载成功')
                    self.fillInformation(_saveFloder, information)
                    self.signUpData.emit(100, '写入Tag成功')
                except Exception as e:
                    self.singError.emit(str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    MainWindow = DownloadMusicWindow(ui)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
