# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:43:47 2022

@author: gldz
"""

import face_recognize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QWidget
class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        self.form=Dialog #用户添加代码
        Dialog.setObjectName("Dialog")
        Dialog.resize(315, 104)
        Dialog.setMinimumSize(QtCore.QSize(315, 104))
        Dialog.setMaximumSize(QtCore.QSize(315, 104))
        Dialog.setAutoFillBackground(False)
        self.Button_Enter = QtWidgets.QPushButton(Dialog)
        self.Button_Enter.setGeometry(QtCore.QRect(221, 21, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_Enter.setFont(font)
        self.Button_Enter.setObjectName("Button_Enter")
        self.Button_Exit=QtWidgets.QPushButton(Dialog)
        self.Button_Exit.setGeometry(QtCore.QRect(221, 54, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_Exit.setFont(font)
        self.Button_Exit.setObjectName("Button_Exit")
        self.face_name=QtWidgets.QLabel(Dialog)
        self.face_name.setGeometry(QtCore.QRect(40, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.face_name.setFont(font)
        self.face_name.setObjectName("face_name")
        self.face_name_frame=QtWidgets.QLineEdit(Dialog)
        self.face_name_frame.setGeometry(QtCore.QRect(30, 40, 167, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.face_name_frame.setFont(font)
        self.face_name_frame.setText("")
        self.face_name_frame.setObjectName("face_name_frame")
 
        self.retranslateUi(Dialog)
        self.Button_Enter.clicked.connect(self.Enter)
        self.Button_Exit.clicked.connect(self.ext)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_Enter.setText(_translate("Dialog", "确认"))
        self.Button_Exit.setText(_translate("Dialog", "退出"))
        self.face_name.setText(_translate("Dialog", "请输入您的姓名："))
 
    def Enter(self):
        fl = open('user_names_admin.txt','a+')
        if self.face_name_frame.text()=="":
            #输入为空时
            reply = QMessageBox.information(self, '提示', '请输入有效用户名', QMessageBox.Ok)
        else:
            fl.write(self.face_name_frame.text()+',')
            fl.close()
 
            reply = QMessageBox.information(self, '提示', '正在采集人脸数据', QMessageBox.Ok)
            face_recognize.Collect_faces()
            reply = QMessageBox.information(self, '提示', '正在训练数据', QMessageBox.Ok)
            face_recognize.Training_faces()
            reply = QMessageBox.information(self, '提示', '人脸信息录入成功', QMessageBox.Ok)
 
 
    def ext(self,event):
        self.form.close()
 
 
if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Dialog=QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())