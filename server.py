# -*- coding: utf-8 -*-
from socket import *
import os
import sys
import signal
import time
from mysqlpython import Mysqlpython

#文件库
FAIL_PATH = "/home/tarena/user_save/"

class TftpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
        self.db = Mysqlpython("tftp")

    def do_login(self,name,passwd):
        '''登录'''
        select = "select name,passwd from user where name=%s"
        result = self.db.all(select,[name])
        if len(result) == 0:
            self.connfd.send(b"nameError")
        else:
            if result[0][1] == passwd:
                self.connfd.send(b"OK")
            else:
                self.connfd.send(b"passwdError")

    def do_register(self,name,passwd):
        '''注册'''
        select = "select name from user where name=%s"
        result = self.db.all(select,[name])
        if len(result) == 0:
            insert = "insert into user(name,passwd) values(%s,%s)"
            result = self.db.zhixing(insert,[name,passwd])
            if result == "OK":
                self.connfd.send(b"OK")
                # 注册成功时在路径下创建该用户的文件夹
                os.mkdir(FAIL_PATH+name)
            else:
                print(result)
                self.connfd.send(b"failed")
        else:
            self.connfd.send(b"exist")

    def do_put(self,name,filename):
        '''客户端上传'''
        with open(FAIL_PATH+name+'/'+filename,"wb") as f:
            while True:
                data = self.connfd.recv(4096)
                if data == b"##*##":
                    data = self.connfd.send(b"OVER")
                    break
                f.write(data)
        # 将文件名大小存入数据库
        try:
            remo = "delete from document where name=%s and filename=%s"
            self.db.zhixing(remo,[name,filename])
            insert = "insert into document(name,filename,filesize) values(%s,%s,%s)"
            filesize = os.path.getsize(FAIL_PATH+name+'/'+filename)
            self.db.zhixing(insert,[name,filename,filesize])
        except Exception as e:
            print(e)

    def decide(self,name,filename):
        # 判断文件是否存在
        filename = filename.split("#*#")
        decide_file = ""
        for x in filename:
            if x != "" and x in os.listdir(FAIL_PATH+name):
                decide_file += x+"#*#"
        if decide_file:
            self.connfd.send(decide_file.encode())
        else:
            self.connfd.send(b"None")

    def showfile(self,name):
        # 返回服务器该用户所有的文件名和文件大小
        files = ""
        for x in os.listdir(FAIL_PATH+name):
            files += x+"#*#"
        if files:
            self.connfd.send(files.encode())
        else:
            self.connfd.send(b"None")

    def remove(self,name,filename):
        # 删除文件
        if filename in os.listdir(FAIL_PATH+name):
            os.remove(FAIL_PATH+name+'/'+filename)
            self.connfd.send(b"OK")
            remo = "delete from document where name=%s and filename=%s"
            self.db.zhixing(remo,[name,filename])
        else:
            self.connfd.send(b"None")

    def do_get(self,name,filename):
        # 客户端下载
        if filename in os.listdir(FAIL_PATH+name):
            self.connfd.send(b"OK")
            time.sleep(0.1)
            with open(FAIL_PATH+name+'/'+filename,"rb") as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        time.sleep(0.1)
                        self.connfd.send(b"##*##")
                        break
                    self.connfd.send(data)
        else:
            self.connfd.send(b"failed")





def main():
    sockfd = socket(AF_INET,SOCK_STREAM)
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(10)
    print("Parent process wait connect")
    #对僵尸进程进行处理
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            connfd,addr = sockfd.accept()
        except Exception as e:
            print(e)
            continue
        print("客户端登录",addr)
        #创建父子进程
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            tftp = TftpServer(connfd)
            while True:
                data = connfd.recv(1024).decode()
                if not data or data[0] == "Q":
                    print(addr,"客户端退出")
                    sys.exit(0)
                elif data[0] == "L":
                    # 登录
                    name = data.split(",")[1]
                    passwd = data.split(",")[2]
                    tftp.do_login(name,passwd)
                elif data[0] == "R":
                    # 注册
                    name = data.split(",")[1]
                    passwd = data.split(",")[2]
                    tftp.do_register(name,passwd)
                elif data[0] == "P":
                    # 客户端上传
                    name = data.split(",")[1]
                    filename = data.split(",")[2:][0]
                    tftp.do_put(name,filename)
                elif data[0] == "D":
                    # 对要上传文件进行判断是否重复
                    name = data.split(",")[1]
                    filename = data.split(',')[2:][0]
                    tftp.decide(name,filename)
                elif data[0] == "S":
                    # 客户端请求文件列表
                    name = data.split(',')[1]
                    tftp.showfile(name)
                elif data[0] == "r":
                    # 删除文件
                    name = data.split(",")[1]
                    filename = data.split(",")[2:][0]
                    tftp.remove(name,filename)
                elif data[0] == "G":
                    # 客户端下载
                    name = data.split(",")[1]
                    filename = data.split(",")[2:][0]
                    tftp.do_get(name,filename)
                else:
                    print("客户端发送了错误指令")
        else:
        # 对于父进程来说，c是无用的
            connfd.close()
            continue





if __name__ == "__main__":
    main()