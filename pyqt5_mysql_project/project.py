# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from time_thread import TimeThread
import pymysql
from project1 import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        #Dialog.resize(528, 484)
        Dialog.setFixedSize(528,484)
        #Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setStyleSheet("")
        # 设置只显示关闭按钮
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        Dialog.setWindowTitle("T_System")
        self.Dg=Dialog
        self.mW = MyWindow()
        #self.mW.sign_down.connect(self.close_window)
        self.umw = Ui_MainWindow()
        self.mW.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.mW.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 250, 461, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.user_layout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.user_layout.setContentsMargins(0, 0, 0, 0)
        self.user_layout.setObjectName("user_layout")
        self.user_label = QtWidgets.QLabel(self.layoutWidget)
        self.user_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_layout.addWidget(self.user_label)
        self.user_edit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.user_edit.setFont(font)
        self.user_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.user_edit.setObjectName("user_edit")
        self.user_layout.addWidget(self.user_edit)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 330, 421, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.password_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.password_layout.setContentsMargins(0, 0, 0, 0)
        self.password_layout.setObjectName("password_layout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.password_layout.addWidget(self.label)
        self.password_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.password_edit.setFont(font)
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")
        self.password_layout.addWidget(self.password_edit)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(140, 410, 301, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.button_layout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setObjectName("button_layout")
        self.in_button = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.in_button.setFont(font)
        self.in_button.setObjectName("in_button")
        self.button_layout.addWidget(self.in_button)
        self.out_button = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.out_button.setFont(font)
        self.out_button.setObjectName("out_button")
        self.button_layout.addWidget(self.out_button)
        self.dele_button=QtWidgets.QPushButton(self.layoutWidget2)
        self.dele_button.setFont(font)
        self.dele_button.setObjectName("dele_button")
        self.button_layout.addWidget(self.dele_button)
        self.in_button.clicked.connect(self.button_response)
        self.out_button.clicked.connect(self.button_response)
        self.dele_button.clicked.connect(self.button_response)
        self.image_widget = QtWidgets.QWidget(Dialog)
        self.image_widget.setGeometry(QtCore.QRect(40, 20, 461, 201))
        self.image_widget.setAutoFillBackground(False)
        self.image_widget.setStyleSheet("""
        #image_widget{
            background-image:url("./baidu.gif");
        }
        #image_label{
            background:black;
            color:gray;
        }
        """)
        self.image_widget.setObjectName("image_widget")
        self.image_label = QtWidgets.QLabel(self.image_widget)
        self.image_label.setGeometry(QtCore.QRect(295, 59, 121, 61))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        #self.image_label.setWindowOpacity(99.0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.tthread=TimeThread()
        self.tthread.t.connect(self.input_image_time)
        self.tthread.start()
        try:
            self.createDB()
            Dialog.setVisible(True)
        except Exception :
            QMessageBox.warning(QtWidgets.QPushButton(),"Warring!","MySQL有误")
            Dialog.setVisible(False)
            self.sthread=ShutDownThread()
            self.sthread.t.connect(self.Dg.close)
            self.sthread.start()


    def input_image_time(self,time):
        self.image_label.setText(time)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.user_label.setText(_translate("Dialog", "用户名:"))
        self.label.setText(_translate("Dialog", "密码:"))
        self.in_button.setText(_translate("Dialog", "登入"))
        self.out_button.setText(_translate("Dialog", "注册"))
        self.dele_button.setText(_translate("Dialog","删除"))

    def createDB(self):
        self.conn = pymysql.connect(host='localhost', user='root')
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("create database %s" % "T_System")
            print("创建库：{},成功".format("T_System"))
        except Exception :
            print("库：{}，已存在".format("T_System"))
        finally:
            self.cursor.execute("use T_System")
            print("使用的当前库：T_System")

        try:
            self.cursor.execute("""create table %s(username varchar(11) not null 
            primary key,password varchar(11) not null)""" % "userlogin")
            print("创建表：{},成功".format("userlogin"))
        except Exception:
            print("表：{}，已存在".format("userlogin"))

    #def close_window(self):
    #    self.Dg.show()


    def button_response(self):
        user_text=self.user_edit.text()
        pass_text=self.password_edit.text()
        if self.sender().objectName()=="in_button":
            if user_text=="" :
                QMessageBox.warning(QtWidgets.QPushButton(),"Warning!","密码或用户名不能为空!")
            else:
                self.cursor.execute("""select * from userlogin 
                where username='%s' and password='%s' """ % (user_text,pass_text))
                if len(self.cursor.fetchall()) > 0:
                    print("跳转")
                    self.Dg.close()


                    self.umw.setupUi(self.mW,self.cursor,self.conn,user_text)
                    self.mW.show()
                    #self.mW.setAttribute(QtCore.Qt.WA_DeleteOnClose)

                    #self.Dg.show()
                else:
                    QMessageBox.warning(QtWidgets.QPushButton(),"Warning!","密码或用户名有误!")
        elif self.sender().objectName()=="out_button":
            if user_text == "" or pass_text == "":
                QMessageBox.warning(QtWidgets.QPushButton(), "Warning!", "密码或用户名不能为空!")
            else:
                self.cursor.execute("""select * from userlogin 
                                where username='%s'""" % user_text)
                if len(self.cursor.fetchall()) > 0:
                    QMessageBox.warning(QtWidgets.QPushButton(),"Warning!","该用户名已存在!")
                else:
                    if len(pass_text)>=6:
                        self.cursor.execute("""insert into userlogin values
                        ('%s','%s')""" % (user_text,pass_text))
                        self.conn.commit()
                        QMessageBox.information(QtWidgets.QPushButton(),"SUCESS!","创建用户成功!")
                    else:
                        QMessageBox.warning(QtWidgets.QPushButton(),"Warinig!","密码不得少于6位!")
        elif self.sender().objectName()=="dele_button":
            if user_text=="" or pass_text=="":
                QMessageBox.warning(QtWidgets.QPushButton(),"Warning!","密码或用户名不能为空!")
            else:
                self.cursor.execute("""select * from userlogin 
                                where username='%s'""" % user_text)
                if len(self.cursor.fetchall()) > 0:
                    self.cursor.execute("""select * from userlogin 
                                    where username='%s' and password='%s' """ % (user_text, pass_text))
                    if len(self.cursor.fetchall()) > 0:
                        y_n = QMessageBox.question(QtWidgets.QPushButton(), '是否删除!', '确认删除吗？',
                                                 QMessageBox.Yes | QMessageBox.No)
                        if y_n == QMessageBox.Yes:
                            self.cursor.execute("delete from userlogin where username='%s'" % user_text)
                            self.conn.commit()
                            QMessageBox.information(QtWidgets.QPushButton(),"SUCESS!","删除用户成功!")
                    else:
                        QMessageBox.warning(QtWidgets.QPushButton(),"Warning!","密码或用户名有误!")
                else:
                    QMessageBox.warning(QtWidgets.QPushButton(),"Warning!","用户不存在!")

    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception :
            pass

class MyWindow(QMainWindow):
    #sign_down=pyqtSignal()
    def __init__(self):
        super(MyWindow,self).__init__(None)
    def closeEvent(self,event):
        #窗口关闭，执行该方法
        #self.sign_down.emit()
        pass

class ShutDownThread(TimeThread):
    def run(self):
        self.msleep(10)
        self.t.emit("")