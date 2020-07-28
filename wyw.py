# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wyw.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file_open = QtWidgets.QPushButton(self.centralwidget)
        self.file_open.setGeometry(QtCore.QRect(20, 10, 321, 23))
        self.file_open.setObjectName("file_open")
        self.True = QtWidgets.QPushButton(self.centralwidget)
        self.True.setGeometry(QtCore.QRect(20, 170, 151, 23))
        self.True.setObjectName("True")
        self.False = QtWidgets.QPushButton(self.centralwidget)
        self.False.setGeometry(QtCore.QRect(190, 170, 151, 23))
        self.False.setObjectName("False")
        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(20, 40, 321, 111))
        self.question.setObjectName("question")
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(20, 200, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.answer.setFont(font)
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setObjectName("answer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 200, 241, 51))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_open.setText(_translate("MainWindow", "파일 불러와서 시작하기"))
        self.True.setText(_translate("MainWindow", "T"))
        self.False.setText(_translate("MainWindow", "F"))
        self.question.setText(_translate("MainWindow", "Questions"))
        self.answer.setText(_translate("MainWindow", "answer"))
        self.label.setText(_translate("MainWindow", "descriptions"))

