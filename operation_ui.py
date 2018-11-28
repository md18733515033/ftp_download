# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operation_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Caozuo(object):
    def setupUi(self, Caozuo):
        Caozuo.setObjectName("Caozuo")
        Caozuo.resize(732, 592)
        Caozuo.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Caozuo)
        self.centralwidget.setObjectName("centralwidget")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(520, 40, 131, 60))
        self.upload.setStyleSheet("font:75 20pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:5px;")
        self.upload.setIconSize(QtCore.QSize(16, 16))
        self.upload.setObjectName("upload")
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(520, 150, 131, 60))
        self.download.setStyleSheet("font:75 20pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:5px;")
        self.download.setObjectName("download")
        self.delete_ui = QtWidgets.QPushButton(self.centralwidget)
        self.delete_ui.setGeometry(QtCore.QRect(520, 270, 131, 60))
        self.delete_ui.setStyleSheet("font:75 20pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:5px;")
        self.delete_ui.setIconSize(QtCore.QSize(16, 16))
        self.delete_ui.setObjectName("delete_ui")
        self.flush = QtWidgets.QPushButton(self.centralwidget)
        self.flush.setGeometry(QtCore.QRect(520, 400, 131, 60))
        self.flush.setStyleSheet("font:75 20pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:5px;")
        self.flush.setIconSize(QtCore.QSize(16, 16))
        self.flush.setObjectName("flush")
        self.cancel_ui = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_ui.setGeometry(QtCore.QRect(629, 489, 91, 51))
        self.cancel_ui.setStyleSheet("font:75 20pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:5px;")
        self.cancel_ui.setIconSize(QtCore.QSize(16, 16))
        self.cancel_ui.setObjectName("cancel_ui")
        self.list_filenames = QtWidgets.QListWidget(self.centralwidget)
        self.list_filenames.setGeometry(QtCore.QRect(30, 60, 381, 441))
        self.list_filenames.setStyleSheet("border-color: rgb(225, 222, 255);\n"
"font: 14pt \"黑体\";\n"
"font-weight:bold;")
        self.list_filenames.setObjectName("list_filenames")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 29, 381, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 18pt \"黑体\";\n"
"font-weighr:bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.04, stop:0.0625 rgba(48, 196, 255, 255));\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # Caozuo.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Caozuo)
        self.statusbar.setObjectName("statusbar")
        # Caozuo.setStatusBar(self.statusbar)

        self.retranslateUi(Caozuo)
        self.upload.clicked.connect(Caozuo.put)
        self.download.clicked.connect(Caozuo.get)
        self.flush.clicked.connect(Caozuo.refresh)
        self.delete_ui.clicked.connect(Caozuo.remove)
        self.cancel_ui.clicked.connect(Caozuo.cancel)
        QtCore.QMetaObject.connectSlotsByName(Caozuo)

    def retranslateUi(self, Caozuo):
        _translate = QtCore.QCoreApplication.translate
        Caozuo.setWindowTitle(_translate("Caozuo", "MainWindow"))
        self.upload.setText(_translate("Caozuo", "上传"))
        self.download.setText(_translate("Caozuo", "下载"))
        self.delete_ui.setText(_translate("Caozuo", "删除"))
        self.flush.setText(_translate("Caozuo", "刷新"))
        self.cancel_ui.setText(_translate("Caozuo", "退出"))
        self.label.setText(_translate("Caozuo", "文件名列表"))

