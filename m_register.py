# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from client import TftpClient
from rejister_ui import Ui_register2
from hashlib import sha1
'''
    注册界面
'''
class Register(QtWidgets.QWidget,Ui_register2,TftpClient,object):
    def __init__(self,tftp):
        super().__init__()
        self.setupUi(self)
        self.tftp = tftp
        # 创建sha1加密对象
        self.s1 = sha1()

    def confirm(self):
        # 注册信息
        name = self.user.text()
        password = self.passwd.text()
        password_2 = self.passwd_2.text()
        if len(name) < 6:
            QMessageBox.warning(self, "warning", "用户名不能少于6位")
        elif not password or len(password) < 6 or len(password) > 18:
            QMessageBox.warning(self, 'warning', '密码格式错误')
        elif password != password_2:
            QMessageBox.warning(self, 'warning', '两次密码输入不一致')
        elif " " in name or " " in password:
            QMessageBox.warning(self, 'warning', '不能包含空格')
        else:
            # 将密码加密发送给服务器
            self.s1.update(password.encode("utf8"))  # 指定编码
            password = self.s1.hexdigest()
            info = self.tftp.do_register(name,password)
            if info == "exist":
                QMessageBox.warning(self, 'warning', '用户名已存在')
            elif info == "failed":
                QMessageBox.warning(self,"warning","注册失败，发生未知错误")
            elif info == "OK":
                QMessageBox.information(self,"恭喜","注册成功")
                self.close()

    def cancel(self):
        # 点击取消的函数
        self.close()
