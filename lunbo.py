# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 23:57:28 2022

@author: gldz
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
import os
import sys

#序列图片轮播，点击图片，打开原图

class MyClass(QtWidgets.QMainWindow):
    def __init__(self,nam):
        super().__init__()
        self.n=1
        self.nam=nam
        self.initUI()

    def initUI(self):
        self.setWindowTitle("百度图片轮播")
        self.resize(400,300)
        global lu
        self.lu = "./"+self.nam+"/"+str(self.n)+".jpg"
        self.pm=QPixmap(self.lu)
        self.lbpic=myLabel(self)
        self.lbpic.setPixmap(self.pm)
        self.lbpic.resize(200,200)
        self.lbpic.move(self.width()/2-self.lbpic.width()/2,50)
        self.lbpic.setScaledContents(True)
        self.lbpic._signal.connect(self.callbacklog)  # 连接信号

        self.timer1=QTimer(self)
        self.timer1.timeout.connect(self.timer_TimeOut)
        self.timer1.start(2000)
        self.show()

    def timer_TimeOut(self):
        pat=os.path.dirname(sys.argv[0])+"/"+self.nam
        self.n+=1
        if self.n>len(os.listdir(pat)):
            self.n=1
        self.lu = "./"+self.nam+"/"+str(self.n)+".jpg"
        self.pm = QPixmap(self.lu)
        self.lbpic.setPixmap(self.pm)

    # 接受信号
    def callbacklog(self, msg):
        from PIL import Image
        import matplotlib.pyplot as plt
        img = Image.open(self.lu)
        plt.figure("image")
        plt.imshow(img)
        plt.show()


class myLabel(QLabel):
    _signal = pyqtSignal(str)#信号定义
    def __init__(self, parent=None):
        super(myLabel, self).__init__(parent)

    # def mousePressEvent(self, e):  ##重载一下鼠标点击事件
    #         print("you clicked the label")
    #         self._signal.emit("正在检测中")

if __name__=="__main__":
    
    app=QApplication(sys.argv)
    nam='向日葵'
    mc=MyClass(nam)
    sys.exit(app.exec_())

