# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word_age.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(683, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vocabulary = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.vocabulary.setGeometry(QtCore.QRect(20, 420, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.vocabulary.setFont(font)
        self.vocabulary.setObjectName("vocabulary")
        self.google_images = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.google_images.setGeometry(QtCore.QRect(450, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.google_images.setFont(font)
        self.google_images.setDescription("")
        self.google_images.setObjectName("google_images")
        self.known = QtWidgets.QPushButton(self.centralwidget)
        self.known.setGeometry(QtCore.QRect(480, 530, 101, 31))
        self.known.setObjectName("known")
        self.easy = QtWidgets.QPushButton(self.centralwidget)
        self.easy.setGeometry(QtCore.QRect(60, 530, 91, 31))
        self.easy.setObjectName("easy")
        self.medium = QtWidgets.QPushButton(self.centralwidget)
        self.medium.setGeometry(QtCore.QRect(200, 530, 91, 31))
        self.medium.setObjectName("medium")
        self.hard = QtWidgets.QPushButton(self.centralwidget)
        self.hard.setGeometry(QtCore.QRect(340, 530, 101, 31))
        self.hard.setObjectName("hard")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 271, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("5401699000140213193505.webp"))
        self.label.setObjectName("label")
        self.status = QtWidgets.QPushButton(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(960, 40, 131, 61))
        self.status.setObjectName("status")
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(210, 250, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.word.setFont(font)
        self.word.setObjectName("word")
        self.meaning = QtWidgets.QLabel(self.centralwidget)
        self.meaning.setGeometry(QtCore.QRect(90, 320, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.meaning.setFont(font)
        self.meaning.setObjectName("meaning")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vocabulary.setText(_translate("MainWindow", "vocabulary.com"))
        self.google_images.setText(_translate("MainWindow", "google images "))
        self.known.setText(_translate("MainWindow", "known"))
        self.easy.setText(_translate("MainWindow", "easy"))
        self.medium.setText(_translate("MainWindow", "medium"))
        self.hard.setText(_translate("MainWindow", "hard"))
        self.status.setText(_translate("MainWindow", "status"))
        self.word.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">TextLabel</span></p></body></html>"))
        self.meaning.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">TextLabel</span></p></body></html>"))

class Word_Page(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Word_Page, self).__init__(parent=parent)
        self.setupUi(self)
