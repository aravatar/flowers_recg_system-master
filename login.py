# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:43:29 2022

@author: gldz
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QWidget
from faces_input_frame import Ui_Dialog
import os
 
 
class Ui_Form(QWidget):  #将object改为QWidget，才能弹出消息对话框
    def __init__(self):
        super(Ui_Form,self).__init__() #用户添加代码
    def setupUi(self, Form):
        self.form=Form  #用户添加代码
        Form.setObjectName("Form")
        Form.setMinimumSize(QtCore.QSize(329, 230))
        Form.setMaximumSize(QtCore.QSize(400, 230))
        Form.setStyleSheet("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(63, 43, 64, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(63, 80, 48, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(121, 80, 133, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(63, 110, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(121, 41, 133, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_face_pass = QtWidgets.QPushButton(Form)
        self.pushButton_face_pass.setGeometry(QtCore.QRect(279, 100, 104, 41))
        self.pushButton_face_pass.setMaximumSize(QtCore.QSize(16777215, 16777213))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_face_pass.setFont(font)
        self.pushButton_face_pass.setObjectName("pushButton_face_pass")
        self.pushButton_face_input = QtWidgets.QPushButton(Form)
        self.pushButton_face_input.setGeometry(QtCore.QRect(280, 31, 104, 41))
        self.pushButton_face_input.setMaximumSize(QtCore.QSize(16777215, 16777213))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_face_input.setFont(font)
        self.pushButton_face_input.setObjectName("pushButton_face_input")
 
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.open)
        self.pushButton_face_input.clicked.connect(self.faceinput)
        self.pushButton_face_pass.clicked.connect(self.facepass)
 
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_2.setText(_translate("Form", "密码："))
        self.pushButton.setText(_translate("Form", "取消"))
        self.pushButton_2.setText(_translate("Form", "确认"))
        self.checkBox.setText(_translate("Form", "记住用户名和密码"))
        self.pushButton_face_pass.setText(_translate("Form", "人脸识别登录"))
        self.pushButton_face_input.setText(_translate("Form", "人脸信息录入"))
 
    def open(self):
        #--------判断用户是否存在--------------
        fl = open('user_names.txt', 'r+')
        pre_name = fl.read()
        fl.close()
        names = pre_name.split(',')
        names = [x.strip() for x in names if x.strip() != '']
        
        password=[]
        for i in range(1,len(names),2):
            password.append(names[i])
            
        nam=[]
        for i in range(0,len(names),2):
            nam.append(names[i])
        
        if self.lineEdit_3.text() in nam:
            # fl = open('password.txt', 'r+')
            # password= fl.read()
            x=nam.index(self.lineEdit_3.text())
            if self.lineEdit_2.text() == password[x]:
                reply=QMessageBox.information(self,'提示','请编写主程序',QMessageBox.Close)
            else:
                reply=QMessageBox.information(self,'提示','密码错误',QMessageBox.Close)
 
 
        else:
            reply=QMessageBox.information(self,'提示','用户不存在',QMessageBox.Close)
 
 
    def close(self, event):
        self.close()
    def faceinput(self,event):
        self.form.hide()
        Form1=QtWidgets.QDialog()
        ui=Ui_Dialog()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
        self.form.show()   #子窗口关闭后，主窗口显示

 
    def facepass(self,event):
        import face_recognize
        get_name=face_recognize.recognize_face()#返回识别的人名
        if get_name=="unknown":
            reply = QMessageBox.information(self, '提示', '人脸识别失败', QMessageBox.Close)
        else:
            reply = QMessageBox.information(self, '提示', "欢迎您："+get_name, QMessageBox.Ok)
            #print("编写其他程序")
            
    def register(self,event):
        self.form.hide()
        Form1=QtWidgets.QDialog()
        ui=Ui_Dialog()
        ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
        self.form.show()   #子窗口关闭后，主窗口显示
 
 
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())