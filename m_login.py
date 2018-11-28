# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from login_ui import Ui_denglu
from PyQt5.QtWidgets import QMessageBox
from client import TftpClient
from m_register import Register
from m_operationer import Operation
from hashlib import sha1
from PyQt5.QtGui import QPalette
'''
    主界面的各种函数的功能
'''

class MainInterface(QtWidgets.QWidget,Ui_denglu,TftpClient,object):
    def __init__(self,tftp):
        super().__init__()
        self.setupUi(self)
        self.tftp = tftp
        # 创建sha1加密对象
        self.s1 = sha1()
    #     self.background_img()
    #
    # def background_img(self):
    #     window_pale = QtGui.QPalette()
    #     window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("800.jpg")))
    #     self.setPalette(window_pale)
    #     self.setAutoFillBackground(True)

    def login(self):
        # 获取输入框内的文本内容
        name = self.user.text()
        password = self.passwd.text()
        if not name:
           #  弹框警告
           QMessageBox.warning(self,"warning","用户名不能为空")
        elif len(name) < 6:
            QMessageBox.warning(self, "warning", "用户名不能少于6位")
        elif not password or len(password) <6 or len(password) > 18:
            QMessageBox.warning(self,'warning','密码格式错误')
        else:
            # 去client里面去进行验证
            # 将密码加密发送给服务器
            self.s1.update(password.encode("utf8"))  # 指定编码
            password = self.s1.hexdigest()
            info = self.tftp.do_login(name,password)
            if info == "OK":
                print("登陆成功")
                try:
                    self.i = Operation(name, self.tftp)
                    self.i.show()
                    # 登录成功调出操作窗口，并将该用户在服务端的文件名展示出来
                    self.i.refresh()
                    self.close()
                except Exception as e:
                    print(e)

            elif info == "nameError":
                QMessageBox.warning(self, 'warning', '用户名不存在')
            elif info == "passwdError":
                QMessageBox.warning(self, 'warning', '密码错误')


    def register(self):
        self.regi = Register(self.tftp)
        self.regi.show()












