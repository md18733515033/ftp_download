# -*- coding: utf-8 -*-
# __author__ = 'djstava@gmail.com'

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from m_login import MainInterface
from socket import *
from client import TftpClient


if __name__ == '__main__':
    '''
    主函数 
    '''

    app = QApplication(sys.argv)
    HOST = '0.0.0.0'
    PORT = 8000
    ADDR = (HOST, PORT)
    sockfd = socket()
    sockfd.connect(ADDR)
    tftp = TftpClient(sockfd)
    myshow = MainInterface(tftp)
    myshow.show()

sys.exit(app.exec_())
