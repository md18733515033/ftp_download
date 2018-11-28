# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rejister_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_register2(object):
    def setupUi(self, register2):
        register2.setObjectName("register2")
        register2.resize(800, 600)
        register2.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(register2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 180, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 230, 51, 21))
        self.label_2.setObjectName("label_2")
        self.user = QtWidgets.QLineEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(270, 170, 251, 31))
        self.user.setStyleSheet("background-color:transparent;\n"
"")
        self.user.setMaxLength(20)
        self.user.setObjectName("user")
        self.passwd = QtWidgets.QLineEdit(self.centralwidget)
        self.passwd.setGeometry(QtCore.QRect(270, 220, 251, 31))
        self.passwd.setStyleSheet("background-color:transparent;")
        self.passwd.setText("")
        self.passwd.setMaxLength(18)
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("passwd")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 280, 54, 12))
        self.label_3.setObjectName("label_3")
        self.passwd_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.passwd_2.setGeometry(QtCore.QRect(270, 270, 251, 31))
        self.passwd_2.setStyleSheet("background-color:transparent;")
        self.passwd_2.setText("")
        self.passwd_2.setMaxLength(18)
        self.passwd_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_2.setObjectName("passwd_2")
        self.zhuce = QtWidgets.QPushButton(self.centralwidget)
        self.zhuce.setGeometry(QtCore.QRect(270, 320, 111, 51))
        self.zhuce.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:5px;")
        self.zhuce.setObjectName("zhuce")
        self.quxiao = QtWidgets.QPushButton(self.centralwidget)
        self.quxiao.setGeometry(QtCore.QRect(410, 320, 111, 51))
        self.quxiao.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:5px;")
        self.quxiao.setObjectName("quxiao")
        # register2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(register2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        # register2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(register2)
        self.statusbar.setObjectName("statusbar")
        # register2.setStatusBar(self.statusbar)

        self.retranslateUi(register2)
        self.zhuce.clicked.connect(register2.confirm)
        self.quxiao.clicked.connect(register2.cancel)
        QtCore.QMetaObject.connectSlotsByName(register2)

    def retranslateUi(self, register2):
        _translate = QtCore.QCoreApplication.translate
        register2.setWindowTitle(_translate("register2", "注册"))
        self.label.setText(_translate("register2", "用户名"))
        self.label_2.setText(_translate("register2", "密码"))
        self.user.setPlaceholderText(_translate("register2", "请输入您的账号"))
        self.passwd.setPlaceholderText(_translate("register2", "请输入6-18位密码(数字，字母，下划线)"))
        self.label_3.setText(_translate("register2", "确认密码"))
        self.passwd_2.setPlaceholderText(_translate("register2", "请输入6-18位密码(数字，字母，下划线)"))
        self.zhuce.setText(_translate("register2", "确定"))
        self.quxiao.setText(_translate("register2", "取消"))

