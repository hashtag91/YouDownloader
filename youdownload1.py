# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youdownload.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from YouDownloader import Download

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color : rgb(194, 196, 195)\n"
"}\n"
"#urlFrame QLineEdit, QLabel{\n"
"    background: transparent;\n"
"    border : none;\n"
"}\n"
"#urlFrame{\n"
"    background-color : white;\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(35, 35))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ico/download.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color : red;")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.urlFrame = QtWidgets.QFrame(self.centralwidget)
        self.urlFrame.setMinimumSize(QtCore.QSize(0, 25))
        self.urlFrame.setMaximumSize(QtCore.QSize(16777215, 35))
        self.urlFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.urlFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.urlFrame.setObjectName("urlFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.urlFrame)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.urlFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(15, 15))
        self.label.setMaximumSize(QtCore.QSize(15, 15))
        self.label.setSizeIncrement(QtCore.QSize(20, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ico/website-https-4951.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.url = QtWidgets.QLineEdit(self.urlFrame)
        self.url.setMinimumSize(QtCore.QSize(0, 15))
        self.url.setMaximumSize(QtCore.QSize(16777215, 15))
        self.url.setObjectName("url")
        self.horizontalLayout_3.addWidget(self.url)
        self.horizontalLayout.addWidget(self.urlFrame)
        self.check = QtWidgets.QToolButton(self.centralwidget)
        self.check.clicked.connect(self.checkFunc)
        self.check.setMinimumSize(QtCore.QSize(80, 20))
        self.check.setMaximumSize(QtCore.QSize(16777215, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico/download.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check.setIcon(icon)
        self.check.setIconSize(QtCore.QSize(12, 12))
        self.check.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.check.setObjectName("check")
        self.horizontalLayout.addWidget(self.check)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titleText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.titleText.setFont(font)
        self.titleText.setAlignment(QtCore.Qt.AlignCenter)
        self.titleText.setObjectName("titleText")
        self.titleText.hide()
        self.verticalLayout_3.addWidget(self.titleText)
        self.tiltle = QtWidgets.QLabel(self.centralwidget)
        self.tiltle.setStyleSheet("background-color: rgba(255,255,255,80);")
        self.tiltle.setText("")
        self.tiltle.setAlignment(QtCore.Qt.AlignCenter)
        self.tiltle.setObjectName("tiltle")
        self.tiltle.hide()
        self.verticalLayout_3.addWidget(self.tiltle)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.hide()
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_9.hide()
        self.horizontalLayout_2.addWidget(self.label_9)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.hide()
        self.horizontalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.taille = QtWidgets.QLabel(self.centralwidget)
        self.taille.setMinimumSize(QtCore.QSize(80, 0))
        self.taille.setStyleSheet("background-color: rgba(255, 255, 255,80);")
        self.taille.setText("")
        self.taille.setAlignment(QtCore.Qt.AlignCenter)
        self.taille.setObjectName("taille")
        self.taille.hide()
        self.horizontalLayout_5.addWidget(self.taille)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.hide()
        self.comboBox.currentTextChanged.connect(self.videoTypeAction)
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.resolutionCombo = QtWidgets.QComboBox(self.centralwidget)
        self.resolutionCombo.setMaximumSize(QtCore.QSize(11111, 20))
        self.resolutionCombo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.resolutionCombo.setObjectName("resolutionCombo")
        self.resolutionCombo.currentTextChanged.connect(self.resComboAction)
        self.resolutionCombo.hide()
        self.horizontalLayout_5.addWidget(self.resolutionCombo)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fileLine = QtWidgets.QLineEdit(self.centralwidget)
        self.fileLine.setStyleSheet("border-radius: 5px;")
        self.fileLine.setObjectName("fileLine")
        self.fileLine.hide()
        self.horizontalLayout_6.addWidget(self.fileLine)
        self.fileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fileBtn.clicked.connect(self.fileDialog)
        self.fileBtn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.fileBtn.setObjectName("fileBtn")
        self.fileBtn.hide()
        self.horizontalLayout_6.addWidget(self.fileBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_8.hide()
        self.horizontalLayout_7.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_7.hide()
        self.horizontalLayout_7.addWidget(self.label_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.telecharge = QtWidgets.QLabel(self.centralwidget)
        self.telecharge.setMaximumSize(QtCore.QSize(16777215, 30))
        self.telecharge.setStyleSheet("background-color: rgba(255,255,255,80);")
        self.telecharge.setText("")
        self.telecharge.setAlignment(QtCore.Qt.AlignCenter)
        self.telecharge.setObjectName("telecharge")
        self.telecharge.hide()
        self.horizontalLayout_8.addWidget(self.telecharge)
        self.restant = QtWidgets.QLabel(self.centralwidget)
        self.restant.setMaximumSize(QtCore.QSize(16777215, 30))
        self.restant.setStyleSheet("background-color: rgba(255,255,255,80);")
        self.restant.setText("")
        self.restant.setAlignment(QtCore.Qt.AlignCenter)
        self.restant.setObjectName("restant")
        self.restant.hide()
        self.horizontalLayout_8.addWidget(self.restant)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.donwloadBtn = QtWidgets.QToolButton(self.centralwidget)
        self.donwloadBtn.setMinimumSize(QtCore.QSize(200, 30))
        self.donwloadBtn.setIcon(icon)
        self.donwloadBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.donwloadBtn.setObjectName("donwloadBtn")
        self.horizontalLayout_9.addWidget(self.donwloadBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "You"))
        self.label_3.setText(_translate("MainWindow", "Downloader"))
        self.url.setPlaceholderText(_translate("MainWindow", "Youtube video url"))
        self.check.setText(_translate("MainWindow", "Check"))
        self.titleText.setText(_translate("MainWindow", "Titre"))
        self.label_5.setText(_translate("MainWindow", "Taille"))
        self.label_9.setText(_translate("MainWindow", "Type"))
        self.label_6.setText(_translate("MainWindow", "Resolution"))
        self.resolutionCombo.setToolTip(_translate("MainWindow", "Resolution"))
        self.fileLine.setPlaceholderText(_translate("MainWindow", "Chemin de destination"))
        self.fileBtn.setText(_translate("MainWindow", "..."))
        self.label_8.setText(_translate("MainWindow", "Téléchargé"))
        self.label_7.setText(_translate("MainWindow", "Restant"))
        self.donwloadBtn.setText(_translate("MainWindow", "Télécharger"))

    def fileDialog(self):
        self.yt = Download(self.url.text())
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        output = dialog.getExistingDirectory(caption='Selectionner un dossier',directory='C:/')
        self.fileLine.setText(f"{output}/{self.yt.VideoTitle()}")
    def checkFunc(self):
        if self.url.text() == "":
            self.urlMsg = QtWidgets.QMessageBox()
            self.urlMsg.setWindowTitle('Information')
            self.urlMsg.setText('Veuillez renseigner le lien de la video\nà vérifier avant le téléchargement')
            self.urlMsg.exec()
        else:
            self.yt = Download(self.url.text())
            videoTitle = self.yt.VideoTitle()
            self.videoRes = self.yt.resList()
            self.videoType = self.yt.videoType()
            self.resolutionCombo.addItems(self.videoRes)
            self.comboBox.addItems(self.videoType)
            self.titleText.show()
            self.tiltle.show()
            self.tiltle.setText(videoTitle)
            self.label_5.show()
            self.label_9.show()
            self.label_6.show()
            self.taille.show()
            self.comboBox.show()
            self.resolutionCombo.show()
            self.fileLine.show()
            self.fileBtn.show()
    def resComboAction(self):
        videoRes = self.yt.resList()
        if self.resolutionCombo.currentText() == videoRes[0]:
            self.videoType = [self.yt.videoType()[0]]
            self.comboBox.clear()
            self.comboBox.addItems(self.videoType)
        else:
            self.videoType = self.yt.videoType()[1::]
            self.comboBox.clear()
            self.comboBox.addItems(self.videoType)
        self.itag = self.yt.itag()
        for it in self.itag:
            if self.resolutionCombo.currentText() in it and self.comboBox.currentText() in it :
                size = round(((self.yt.streams.get_by_itag(it[0]).filesize/1024)/1024),1)
                self.taille.setText(f"{size} Mo")
                break
    def videoTypeAction(self):
        self.itag = self.yt.itag()
        for it in self.itag:
            if self.resolutionCombo.currentText() in it and self.comboBox.currentText() in it :
                size = int((self.yt.streams.get_by_itag(it[0]).filesize/1024)/1024)
                self.taille.setText(f"{size} Mo")
                break
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
