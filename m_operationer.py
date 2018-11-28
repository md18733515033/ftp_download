# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from operation_ui import Ui_Caozuo
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import os
from threading import Thread


class Operation(Ui_Caozuo,QtWidgets.QWidget,object):
    def __init__(self,name,tftp):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.tftp = tftp

    def put(self):
        # 使用多线程，失败
        try:
            t = Thread(target=self.threadput())
            t.setDaemon(True)
            t.start()
            t.join()
        except Exception as e:
            print(e)

        '''getOpenFileName第一个参数是self
        第二参数是文件读取框的名字。
        第三参数是默认的路径。（windows用户需要稍微一下）
        -----------------------------------------------------------------------
        返回的两个参数，第一个参数是选择的文件的文件名
        第二个参数是状态，当正确选择文件名后才会返回True，否则返回False，用以判断是否读取成功。
        '''
    def threadput(self):
        filenames,filetype= QtWidgets.QFileDialog.getOpenFileNames(self,
                                                  "多文件选择",
                                                  "c:/")
        print(filenames)
        if filenames:
            data = self.tftp.decide(self.name,filenames)
            # 判断选取的文件是否在服务端存在
            if data != "None":
                chongfu_file = data.split("#*#")
                # 用来存储重复的文件名
                files = ''
                for x in chongfu_file:
                    if x != '':
                        files += x+"   "
                reply = QMessageBox.question(self, "warning", files+"文件已存在，是否进行覆盖?", QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    info = self.tftp.do_put(self.name, filenames)
                    if info == "OVER":
                        self.refresh()
                        QMessageBox.information(self, "恭喜", "上传成功")
                    elif info == "failed":
                        QMessageBox.warning(self, "warning","上传失败")
                else:
                    pass
            else:
                info = self.tftp.do_put(self.name, filenames)
                if info == "OVER":
                    self.refresh()
                    QMessageBox.information(self, "恭喜", "上传成功")
                elif info == "failed":
                    QMessageBox.warning(self, "warning","上传失败")


    def get(self):
        '''下载文件'''
        getFile = self.list_filenames.currentItem()
        if getFile:
            get_file = getFile.text()
            reply = QMessageBox.question(self, "enquiry", "是否下载" + get_file + "?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                directory_save = QFileDialog.getExistingDirectory(self,"请选择要保存的路径","C:/")
                if directory_save:
                    if get_file in os.listdir(directory_save):
                        # 选取文件夹后判断该文件夹下是否有同名的文件
                        reply = QMessageBox.information(self,"warning","该目录下已存在该文件，继续下载将会覆盖，是否继续？",QMessageBox.Yes | QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            info = self.tftp.do_get(self.name, get_file,directory_save)
                            if info == "OVER":
                                QMessageBox.information(self, "提示", get_file + "下载成功", QMessageBox.Yes)
                                # 下载后自动刷新列表显示
                                self.refresh()
                            else:
                                QMessageBox.information(self, "warning", get_file + "文件不存在", QMessageBox.Yes)
                    else:
                        #没有同名文件直接下载
                        info = self.tftp.do_get(self.name, get_file, directory_save)
                        if info == "OVER":
                            QMessageBox.information(self, "提示", get_file + "下载成功", QMessageBox.Yes)
                            # 下载后自动刷新列表显示
                            self.refresh()
                        else:
                            QMessageBox.information(self, "warning", get_file + "文件不存在", QMessageBox.Yes)
                else:
                    pass
            else:
                pass
        else:
            QMessageBox.warning(self, "warning", "请选择要下载的文件")

    def refresh(self):
        '''刷新列表'''
        # 每次刷新先清空列表再进行写入，否则会重复
        self.list_filenames.clear()
        data = self.tftp.showfile(self.name)
        if data != "None":
            fileList = data.split("#*#")
            file_list=[]
            for x in fileList:
                if x != "":
                    file_list.append(x)
            # 对服务器返回的已有列表进行排序
            file_list.sort()
            # 将服务器返回的文件名显示在界面上
            for x in file_list:
                self.list_filenames.addItem(x)
        else:
            pass

    def remove(self):
        '''删除'''
        # 获取选中的文件的对象，.text()查看文本
        removeFile = self.list_filenames.currentItem()
        if removeFile:
            remove_file = removeFile.text()
            reply = QMessageBox.question(self, "warning", "是否删除"+remove_file+"?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                info = self.tftp.do_remove(self.name,remove_file)
                if info == "OK":
                    QMessageBox.information(self, "提示", remove_file+"删除成功", QMessageBox.Yes)
                    # 删除后自动刷新列表显示
                    self.refresh()
                else:
                    QMessageBox.information(self,"warning",remove_file+"文件不存在，请刷新后重试",QMessageBox.Yes)
            else:
                pass
        else:
            QMessageBox.warning(self,"warning","请选择要删除的文件")


    def cancel(self):
        '''退出'''
        info = QMessageBox.information(self,"quit","小主，确定要退出吗",QMessageBox.Yes,QMessageBox.No)
        if info == QMessageBox.Yes:
            self.tftp.do_cancel()
            self.close()
        else:
            pass



