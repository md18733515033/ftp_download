# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_denglu(object):
    def setupUi(self, denglu):
        denglu.setObjectName("denglu")
        denglu.resize(800, 600)
        denglu.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(denglu)
        self.centralwidget.setObjectName("centralwidget")
        self.login_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.login_buttom.setGeometry(QtCore.QRect(270, 390, 111, 51))
        self.login_buttom.setStyleSheet("font:75 16pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:5px;\n"
"font-weight:bold;")
        self.login_buttom.setObjectName("login_buttom")
        self.request_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.request_buttom.setGeometry(QtCore.QRect(410, 390, 111, 51))
        self.request_buttom.setStyleSheet("font:75 16pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:5px;\n"
"font-weight:bold;")
        self.request_buttom.setObjectName("request_buttom")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 230, 91, 20))
        self.label.setStyleSheet("font: 12pt;\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 280, 51, 21))
        self.label_2.setStyleSheet("font: 12pt;\n"
"font-weight:bold;")
        self.label_2.setObjectName("label_2")
        self.user = QtWidgets.QLineEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(270, 229, 251, 31))
        self.user.setStyleSheet("background-color:transparent;\n"
"")
        self.user.setMaxLength(20)
        self.user.setObjectName("user")
        self.passwd = QtWidgets.QLineEdit(self.centralwidget)
        self.passwd.setGeometry(QtCore.QRect(270, 270, 251, 31))
        self.passwd.setStyleSheet("background-color:transparent;")
        self.passwd.setText("")
        self.passwd.setMaxLength(16)
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("passwd")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(270, 340, 71, 31))
        self.checkBox.setObjectName("checkBox")
        # denglu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(denglu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        # denglu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(denglu)
        self.statusbar.setObjectName("statusbar")
        # denglu.setStatusBar(self.statusbar)

        self.retranslateUi(denglu)
        self.login_buttom.clicked.connect(denglu.login)
        self.request_buttom.clicked.connect(denglu.register)
        QtCore.QMetaObject.connectSlotsByName(denglu)

    def retranslateUi(self, denglu):
        _translate = QtCore.QCoreApplication.translate
        denglu.setWindowTitle(_translate("denglu", "MainWindow"))
        self.login_buttom.setText(_translate("denglu", "登录"))
        self.request_buttom.setText(_translate("denglu", "注册"))
        self.label.setText(_translate("denglu", "用户名"))
        self.label_2.setText(_translate("denglu", "密码"))
        self.user.setPlaceholderText(_translate("denglu", "请输入您的账号"))
        self.passwd.setPlaceholderText(_translate("denglu", "请输入6-18位密码(数字，字母，下划线)"))
        self.checkBox.setText(_translate("denglu", "记住密码"))

