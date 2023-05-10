# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:34:44 2022

@author: gldz
"""

import sys
from PyQt5.QtWidgets import(QWidget,QApplication,QGridLayout,QLabel,
                            QLineEdit,QTextEdit,QPushButton,QFrame,QFileDialog,QDialog)
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QFont

import torch
from model import AlexNet
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import json
from bdbk import look_up
from papic import Picture
from papic2 import code
import os
from os import path
import time
from lunbo import MyClass
from wordcloud import WordCloud
from imageio import imread


class AIGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #关于表格类的相关初始化代码
        #setSpacing 就是设置每个控件的外边框
        grid=QGridLayout()
        grid.setSpacing(10)
        
        font = QFont()
        font.setPointSize(10)  # 括号里的数字可以设置成自己想要的字体大小
        font.setFamily("Microsoft YaHei")  # 雅黑体
        
        #各个控件
        #1号控件
        explain=QLabel('请选择要识别的图片')
        explain.setFont(font)
        #2号 单号文本框
        self.imgUrl=QLineEdit()
        #3号，按钮
        self.select=QPushButton("浏览")
        self.select.setFont(font)
        #为按钮添加一个事件处理函数
        self.select.clicked.connect(self.openfile)
        #4号，图片框
        self.imgLab=QLabel("图片文件")
        self.imgLab.setFont(font)
        self.imgLab.setFrameShape(QFrame.Box)
        #self.imgLab.setFrameShadow(QFrame.Raised)
        self.imgLab.setLineWidth(1)
        #5
        self.info=QTextEdit()
        self.info.setFont(font)
        #6
        self.imgLab_2=QLabel("植物科学数据中心二维码")
        self.imgLab_2.setFont(font)
        self.imgLab_2.setFrameShape(QFrame.Box)
        #self.imgLab_2.setFrameShadow(QFrame.Raised)
        self.imgLab_2.setLineWidth(1)

        self.imgLab_3=QLabel("词云图")
        self.imgLab_3.setFont(font)
        self.imgLab_3.setFrameShape(QFrame.Box)
        #self.imgLab_2.setFrameShadow(QFrame.Raised)
        self.imgLab_3.setLineWidth(1)

        #将控件进行合理布局
        grid.addWidget(explain,1,0)
        grid.addWidget(self.imgUrl,1,1)
        grid.addWidget(self.select,1,2)
        grid.addWidget(self.imgLab,2,0,2,1)
        grid.addWidget(self.info,2,1,4,1)
        grid.addWidget(self.imgLab_2,4,0,2,1)
        grid.addWidget(self.imgLab_3,2,2,4,1)
 
        #窗口最后的设置
        self.setLayout(grid)
        
        self.setGeometry(300,300,1200,800)
        self.setWindowTitle("植物识别")
        self.show()
    def openfile(self):
        #打开图片弹窗，选择图片
        self.select_path=QFileDialog.getOpenFileName(self,"选择要识别的图片","/","Imgae Files(*.jpg *.jpeg)")
        #如果没选择图片，空过
        if not self.select_path[0].strip():
            pass
        else:
            #选择图片后执行下面的内容
            # 设置图片的路径
            self.imgUrl.setText(self.select_path[0])
            #在图片标签框中显示图片
            #1)根据路径pixmap解析图片
            pixmap=QPixmap(self.select_path[0])
            #2)缩放图片
            scalePixmap=pixmap.scaledToWidth(300)
            #scaledPixmap=pixmap.scaled(QSize(311,301))
            #3)显示
            self.imgLab.setPixmap(scalePixmap)
            result=self.identify()
            self.info.setText(result)
     
    
    def show_new_window(self,nam):
        self.w = MyClass(nam)
        self.w.show()
        
        
    def identify(self):
        
        data_transform = transforms.Compose(
            [transforms.Resize((224, 224)),
             transforms.ToTensor(),
             transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        
        img = Image.open(self.select_path[0])
        img = data_transform(img)
        img = torch.unsqueeze(img, dim=0)
         
        try:
            json_file = open('./class_indices.json', 'r')
            class_indict = json.load(json_file)
        except Exception as e:
            print(e)
            exit(-1)
         

        model = AlexNet(num_classes=5)
        model_weight_path = "./AlexNet.pth"
        #, map_location='cpu'
        model.load_state_dict(torch.load(model_weight_path, map_location='cpu'))
        
        # 关闭 Dropout
        model.eval()
        with torch.no_grad():
            # predict class
            output = torch.squeeze(model(img))    # 将输出压缩，即压缩掉 batch 这个维度
            predict = torch.softmax(output, dim=0)
            predict_cla = torch.argmax(predict).numpy()
        print(class_indict[str(predict_cla)], '相似度：'+str(100*float(predict[predict_cla].item()))+'%')
        if str(class_indict[str(predict_cla)])=='daisy':
            nam='菊花'
        if str(class_indict[str(predict_cla)])=='dandelion':
            nam='蒲公英'
        if str(class_indict[str(predict_cla)])=='roses':
            nam='玫瑰'
        if str(class_indict[str(predict_cla)])=='sunflowers':
            nam='向日葵'
        if str(class_indict[str(predict_cla)])=='tulips':
            nam='郁金香'
        
        pic=Picture()            
        totalnum=10
        pic.run(nam,totalnum)
        code(nam)
        
        url='./'+nam
        # #遍历当前路径下所有文件
        # file  = os.listdir(url)
        # #字符串拼接
        # real_url = path.join (url , f)
        
        real_url = url+'/0.png'
        #1)根据路径pixmap解析图片
        pixmap=QPixmap(real_url)
        #2)缩放图片
        scalePixmap=pixmap.scaledToWidth(300)
        #scaledPixmap=pixmap.scaled(QSize(311,301))
        #3)显示
        self.imgLab_2.setPixmap(scalePixmap)
        # time.sleep(2)
        
        bdbk_result=look_up(nam)
        #######################################词云图
        mask=imread('1.jpg')
        txt=bdbk_result
        wordcloud=WordCloud(background_color="white",\
                    font_path='C:\\Windows\\Fonts\\simfang.ttf',\
                    width=800,\
                    height=600,\
                    max_words=1000,\
                    max_font_size=80,\
                    mask=mask)
        wordcloud.generate_from_text(txt)
        wordcloud.to_file(nam+'/'+nam+'.png')
        #1)根据路径pixmap解析图片
        pixmap=QPixmap(nam+'/'+nam+'.png')
        #2)缩放图片
        scalePixmap=pixmap.scaledToWidth(500)
        #scaledPixmap=pixmap.scaled(QSize(311,301))
        #3)显示
        self.imgLab_3.setPixmap(scalePixmap)
        ########################################
        result=nam+' 相似度：'+str(100*float(predict[predict_cla].item()))+'%'+'\n'+bdbk_result
        
        self.show_new_window(nam)
        # app=QApplication(sys.argv)
        # mc=MyClass(nam)
        # sys.exit(app.exec_())
        # Form2=QDialog()
        # ui=MyClass(nam)
        # # ui.initUI(Form2)
        # Form2.show()
        # # Form2.exec_()
        
        return result

 
def main():
    app=QApplication(sys.argv)
    ai=AIGUI()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main()
    
    
    
    
    