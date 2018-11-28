from socket import *
import sys
import time
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
'''
    客户端
'''
class TftpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def do_login(self,name,passwd):
        '''登录'''
        # 发送用户名密码给客户端进行验证
        self.sockfd.send(("L,"+name+','+passwd).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            # print("登陆成功")
            return 'OK'
        elif data == "nameError":
            # print("用户名错误")
            return "nameError"
        elif data == "passwdError":
            # print("密码错误")
            return "passwdError"

    def do_register(self,name,passwd):
        '''注册'''
        self.sockfd.send(("R,"+name+","+passwd).encode())
        data = self.sockfd.recv(1024).decode()
        return data

    def do_put(self,name,filenames):
        '''上传'''
        for x in filenames:
            file = x.split("/")[-1]
            self.sockfd.send(("P,"+name+","+file).encode())
            time.sleep(0.1)
            with open(x, "rb") as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        time.sleep(0.1)
                        self.sockfd.send(b"##*##")
                        break
                    self.sockfd.send(data)
                data = self.sockfd.recv(1024).decode()
                if data == "OVER":
                    # 当文件上传成功时继续上传下一个文件
                    continue
                else:
                    return "failed"
        return "OVER"

    def do_get(self,name,file,path):
        '''下载'''
        self.sockfd.send(("G,"+name+","+file).encode())
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            with open(path+"/"+file,"wb") as f:
                while True:
                    data = self.sockfd.recv(4096)
                    if data == b"##*##":
                        return "OVER"
                    f.write(data)
        else:
            return data

    def do_remove(self,name,file):
        '''删除'''
        self.sockfd.send(("r,"+name+','+file).encode())
        data = self.sockfd.recv(1024).decode()
        print(data)
        return data


    def decide(self,name,filenames):
        #判断服务器是否已经有要上传的文件
        filename = ""
        for x in filenames:
            file = x.split("/")[-1]+"#*#"
            filename += file
        self.sockfd.send(("D,"+name+","+filename).encode())
        data = self.sockfd.recv(4096).decode()
        return data

    def showfile(self,name):
        '''向服务器索要已存在的文件名称'''
        self.sockfd.send(("S,"+name).encode())
        data = self.sockfd.recv(4096).decode()
        return data

    def do_cancel(self):
        # 客户端退出之前告知服务端
        self.sockfd.send(b"Q")



