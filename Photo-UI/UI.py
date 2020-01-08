# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageTk
from PyQt5.QtGui import QImage, QPixmap
import cv2
import os


class Ui_MainWindow(object):

    def __init__(self):
        self.zoomscale = 1  # 图片放缩尺度
        self.Hr_file_path = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 360, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 350, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 54, 16))
        self.label_3.setObjectName("label_3")
        self.choose = QtWidgets.QPushButton(self.centralwidget)
        self.choose.setGeometry(QtCore.QRect(330, 20, 70, 23))
        self.choose.setObjectName("choose")

        self.choose.clicked.connect(self.open_file)

        self.fileroad = QtWidgets.QTextBrowser(self.centralwidget)
        self.fileroad.setEnabled(True)
        self.fileroad.setGeometry(QtCore.QRect(70, 20, 256, 21))
        self.fileroad.setMouseTracking(False)
        self.fileroad.setTabletTracking(False)
        self.fileroad.setAcceptDrops(True)
        self.fileroad.setObjectName("fileroad")

        self.original = QtWidgets.QGraphicsView(self.centralwidget)
        self.original.setGeometry(QtCore.QRect(30, 60, 371, 291))
        self.original.setObjectName("original")

        self.new_photo = QtWidgets.QGraphicsView(self.centralwidget)
        self.new_photo.setGeometry(QtCore.QRect(550, 50, 401, 291))
        self.new_photo.setObjectName("new_photo")

        self.enlarge = QtWidgets.QPushButton(self.centralwidget)
        self.enlarge.setGeometry(QtCore.QRect(440, 170, 70, 23))
        self.enlarge.setObjectName("enlarge")

        self.enlarge.clicked.connect(self.enlarge_size)

        self.new_photo_rezize = QtWidgets.QGraphicsView(self.centralwidget)
        self.new_photo_rezize.setGeometry(QtCore.QRect(550, 370, 401, 291))
        self.new_photo_rezize.setObjectName("new_photo_rezize")

        self.resize = QtWidgets.QLabel(self.centralwidget)
        self.resize.setGeometry(QtCore.QRect(730, 660, 54, 12))
        self.resize.setObjectName("resize")

        self.number = QtWidgets.QTextBrowser(self.centralwidget)
        self.number.setEnabled(True)
        self.number.setGeometry(QtCore.QRect(1000, 630, 61, 31))
        self.number.setMouseTracking(False)
        self.number.setTabletTracking(False)
        self.number.setAcceptDrops(True)
        self.number.setObjectName("number")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "原图"))
        self.label_2.setText(_translate("MainWindow", "SR"))
        self.label_3.setText(_translate("MainWindow", "LR photo:"))
        self.choose.setText(_translate("MainWindow", "choose"))
        self.enlarge.setText(_translate("MainWindow", "放大"))
        self.resize.setText(_translate("MainWindow", "resize"))


    def open_file(self):
        self.org_photo, _ = QFileDialog.getOpenFileName(ui.choose, "选择文件", "/", "图片文件 (*.png);;(*.jpeg)")
        self.fileroad.clear()
        self.fileroad.insertPlainText("%s" % self.org_photo)
        self.ori_img_show()

    def ori_img_show(self):

        self.img_old = cv2.imread(self.org_photo)  # 读取图像
        self.img = cv2.cvtColor(self.img_old, cv2.COLOR_BGR2RGB)  # 转换图像通道

        self.height_old, self.width_old = self.img.shape[:2]
        widthStep = self.width_old * 3
        self.frame = QtGui.QImage(self.img, self.width_old, self.height_old, widthStep, QtGui.QImage.Format_RGB888)

        self.pix = QPixmap.fromImage(self.frame)
        self.item = QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.original.setScene(self.scene)  # 将场景添加至视图

    def Hr_img_show(self):

        img2 = cv2.imread(self.Hr_file_path + '/img' + '/img_005_SRF_x%s_SR.png' % self.zoomscale)  # 读取图像
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)  # 转换图像通道

        height, width = img2.shape[:2]
        widthStep = width * 3
        frame2 = QtGui.QImage(img2, width, height, widthStep, QtGui.QImage.Format_RGB888)

        pix2 = QPixmap.fromImage(frame2)
        item2 = QGraphicsPixmapItem(pix2)  # 创建像素图元
        scene2 = QGraphicsScene()  # 创建场景
        scene2.addItem(item2)
        self.new_photo.setScene(scene2)  # 将场景添加至视图

    def enlarge_size(self):

        self.zoomscale = self.zoomscale + 0.1
        if self.zoomscale > 4:
            self.zoomscale = 4.0
        self.zoomscale = round(self.zoomscale,1)
        # print(self.zoomscale)

        size = (int(self.width_old / self.zoomscale), int(self.height_old / self.zoomscale))
        enlarge_CUBIC = cv2.resize(self.img_old, size, interpolation=cv2.INTER_CUBIC)
        enlarge_CUBIC = cv2.resize(enlarge_CUBIC, (0, 0), fx=self.zoomscale, fy=self.zoomscale, interpolation=cv2.INTER_CUBIC)
        # cv2.imwrite('x%s_SR.png' % self.zoomscale, enlarge_CUBIC)

        enlarge_CUBIC = cv2.cvtColor(enlarge_CUBIC, cv2.COLOR_BGR2RGB)  # 转换图像通道
        height, width = enlarge_CUBIC.shape[:2]
        widthStep = width * 3
        self.frame1 = QtGui.QImage(enlarge_CUBIC, width, height, widthStep, QtGui.QImage.Format_RGB888)

        self.pix1 = QPixmap.fromImage(self.frame1)
        self.item1 = QGraphicsPixmapItem(self.pix1)  # 创建像素图元
        self.scene1 = QGraphicsScene()  # 创建场景
        self.scene1.addItem(self.item1)
        self.new_photo_rezize.setScene(self.scene1)  # 将场景添加至视图
        self.Hr_img_show()

        self.number.clear()
        self.number.insertPlainText("%s" % self.zoomscale)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
