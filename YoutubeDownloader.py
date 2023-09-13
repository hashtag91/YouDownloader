from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import icon
import sys
from pytube import YouTube, query
import requests
import speedtest

class ThreadClass1(QThread):
    checkAction = pyqtSignal(list)
    stream_info = pyqtSignal(query.StreamQuery)
    def __init__(self,url:str):
        super().__init__()
        self.url = url
    def run(self):
        self.yt = YouTube(self.url)
        self.stream = self.yt.streams
        itag = self.stream.itag_index
        itag_list = [x.real for x in itag]
        thumbnailurl = self.yt.thumbnail_url
        self.data_list = [self.yt.title,itag_list,thumbnailurl]
        self.checkAction.emit(self.data_list)
        self.stream_info.emit(self.stream)
        
class SpeedTextThread(QThread):
    speed = pyqtSignal(list)
    def __init__(self):
        super().__init__()
    def run(self):
        while True:
            try:
                self.down = round(speedtest.Speedtest().download() / 1000 / 1000,1)
                self.up = round(speedtest.Speedtest().upload() /1000 /1000,1)
                self.speedtest_result = [self.down, self.up]
                self.speed.emit(self.speedtest_result)
            except:
                text = ["Error occurred while refreshing connection speed"]
                self.speed.emit(text)
                break

class downloadThread(QThread):
    percent_slot = pyqtSignal(int)
    def __init__(self,url,it,path):
        super().__init__()
        self.url = url
        self.it = it
        self.path = path
    def run(self):
        self.yt = YouTube(self.url)
        self.stream = self.yt.streams.get_by_itag(self.it)
        self.yt.register_on_progress_callback(self.progress)
        self.stream.download(self.path)
    def progress(self,stream, chunk, bytes_remaining):
        percent = (stream.filesize - bytes_remaining) / (stream.filesize / 100)
        self.percent_slot.emit(percent)
        
class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow,self).__init__()
        uic.loadUi('MainWindow.ui',self,resource_suffix='qrc')
        self.res_list = {17:"144p",18:"360p",22:"720p",137:"1080p",140:"Audio"}
        self.itag = 0
        sp = SpeedTextThread()
        sp.speed.connect(self.speedtext_func)
        sp.start()
        self.check_btn.clicked.connect(self.check_fun)
        self.resolution.currentTextChanged.connect(self.resolution_func)
        self.stream = query.StreamQuery
        self.file_button.clicked.connect(self.download_folder_func)
        self.download_btn.clicked.connect(self.download_func)
        self.show()
        
    def check_fun(self):
        self.checkThread = ThreadClass1(self.search_line.text())
        self.console_browser.append('<span style="color: green">Search launched please waint for the result...</span>')
        self.checkThread.checkAction.connect(self.check_func_off)
        self.checkThread.start()
    def check_func_off(self,info:list):
        try:
            self.video_title_text.setText(info[0])
            self.resolution.clear()
            for _ in info[1]:
                if _ in self.res_list:
                    self.resolution.addItem(self.res_list[_])
            image = QImage()
            image.loadFromData(requests.get(f"{info[2]}").content)
            self.thumbnail.setPixmap(QPixmap(image))
        except:
            self.console_browser.append("<span style='color: red;'>Something went wrong</span>")
    
    def resolution_func(self):
        self.console_browser.append("<span style='color: black;'>Size display updating... running</span>")
        self.size_thread = ThreadClass1(self.search_line.text())
        self.size_thread.stream_info.connect(self.resolution_func_off)
        self.size_thread.start()
    def resolution_func_off(self,val):
        for i in self.res_list:
            if self.res_list[i] == self.resolution.currentText():
                self.itag = i
                file_size = round((val.get_by_itag(i).filesize/1000)/1000,1)
        self.size_label_text.setText(f" {file_size} MB")
        self.console_browser.append("<span style='color: green;'>Size display updating... done !</span>")
    
    def download_folder_func(self):
        self.folder = QFileDialog.getExistingDirectory(self,"Open directory","C:/")
        self.directory_line.setText(self.folder)
        
    def speedtext_func(self,val:list):
        if len(val) == 2:
            self.download_label.setText(f"{val[0]} Mbit/s")
            self.upload_label.setText(f"{val[1]} Mbit/s")
        else:
            self.console_browser.append(f"<span style='color: red;'>{val[0]}</span>")
    """        
    def progress_func(self, chunk, bytes_remaining):
            progress = progressThread(self.itag)
            progress.progress.connect(self.progress_func_off)
            progress.start()
    def progress_func_off(self,val):
        self.progressBar.setValue(val)
"""
    def download_func(self):
        if self.directory_line.text() == "":
            self.download_folder_func()
            self.console_browser.append(f"<span style='color: black;'>Downloading... </span>")
            self.progressBar.setFormat("Download preparing...")
            self.dl = downloadThread(self.search_line.text(),self.itag,self.directory_line.text())
            self.dl.percent_slot.connect(self.progress_func)
            self.dl.start()
        else:
            self.console_browser.append(f"<span style='color: black;'>Downloading... </span>")
            self.progressBar.setFormat("Download preparing...")
            self.dl = downloadThread(self.search_line.text(),self.itag,self.directory_line.text())
            self.dl.percent_slot.connect(self.progress_func)
            self.dl.start()
    def progress_func(self,val):
        self.progressBar.setFormat("Preparing to download...")
        if val < 99:
            self.progressBar.setValue(val)
            self.progressBar.setFormat(f"{val} %")
        else:
            self.progressBar.setValue(100)
            self.progressBar.setFormat("Completed")
            self.console_browser.append(f"<span style='color: green;'>Download completed succefully ! </span>")
        
if __name__ == "__main__":
    App = QApplication(sys.argv)
    w = mainWindow()
    sys.exit(App.exec())