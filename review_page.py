# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 508)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(100, 350, 641, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.meaning = QtWidgets.QLabel(self.centralwidget)
        self.meaning.setGeometry(QtCore.QRect(100, 130, 621, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.meaning.setFont(font)
        self.meaning.setObjectName("meaning")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(180, 260, 451, 51))
        self.input.setObjectName("input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REVIEW PAGE"))
        self.check.setText(_translate("MainWindow", "check"))
        self.meaning.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>"))


class Review_Page(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Review_Page, self).__init__(parent=parent)
        self.setupUi(self)
