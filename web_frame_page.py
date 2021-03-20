import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QLineEdit, QMainWindow,
    QPushButton, QToolBar)
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class Web_Frame(QMainWindow):

    def __init__(self):
        super(Web_Frame, self).__init__()

        self.initUI()


    def initUI(self):
        self.resize(700, 800)
        self.toolBar = QToolBar(self)
        self.addToolBar(self.toolBar)
        self.backBtn = QPushButton(self)
        self.backBtn.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/left-32.png'))
        self.backBtn.setIconSize(QSize(50,50))
        self.backBtn.setIconSize(QSize(50,50))
        self.backBtn.clicked.connect(self.back)
        self.toolBar.addWidget(self.backBtn)

        self.webEngineView = QWebEngineView(self)
        self.setCentralWidget(self.webEngineView)

        #self.webEngineView.page().urlChanged.connect(self.onLoadFinished)
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
#        self.webEngineView.page().urlChanged.connect(self.urlChanged)

        #self.setGeometry(500, 200, 1000, 800)
        self.setWindowTitle('QWebEnginePage')


    def load(self,url):

        url = QUrl(url)
        if url.isValid():
            self.webEngineView.load(url)
        self.show()

    def back(self):
        self.hide()



