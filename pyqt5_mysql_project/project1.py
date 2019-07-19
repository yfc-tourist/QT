# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from image_download import Image_download
from PyQt5.QtWidgets import QAction,QDialog


class Ui_MainWindow(object):

    def setupUi(self, MainWindow,cursor,conn,usertext):
        self.cursor=cursor
        self.usertext=usertext
        self.conn=conn
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 266)
        self.Mw = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.process_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.process_bar.setGeometry(QtCore.QRect(60, 200, 191, 23))
        self.process_bar.setProperty("value", 24)
        self.process_bar.setObjectName("process_bar")
        self.process_bar.setValue(0)
        self.process_bar.setMinimum(0)
        self.image_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.image_edit.setGeometry(QtCore.QRect(130, 50, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.image_edit.setFont(font)
        self.image_edit.setObjectName("image_edit")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(130, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.crawl_button = QtWidgets.QPushButton(self.centralwidget)
        self.crawl_button.setGeometry(QtCore.QRect(90, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.crawl_button.setFont(font)
        self.crawl_button.setObjectName("crawl_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 261, 18))
        self.menubar.setObjectName("menubar")
        self.menu_main = QtWidgets.QMenu(self.menubar)
        self.menu_main.setObjectName("menu_main")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.username = QtWidgets.QAction(MainWindow)
        self.username.setObjectName("username")
        self.password = QtWidgets.QAction(MainWindow)
        self.password.setObjectName("password")
        self.menu_main.addAction(self.username)
        self.menu_main.addAction(self.password)
        self.menubar.addAction(self.menu_main.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.crawl_button.clicked.connect(self.download_image)
        self.image_object=Image_download()
        self.image_object.sign.connect(self.process_bar_add)
#       阶段
        self.dialog = QDialog()
        self.menu_main.triggered[QAction].connect(self.processtrigger)
        self.save = QtWidgets.QPushButton(self.dialog)
        self.save.setGeometry(QtCore.QRect(285, 216, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.save.setText("Save")

        self.label = QtWidgets.QLabel(self.dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 71, 31))
        self.font = QtGui.QFont()
        self.font.setPointSize(30)
        self.label.setFont(self.font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 71, 31))
        self.label_2.setFont(self.font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 181, 20))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.save.clicked.connect(self.save_)



    def download_image(self):
        word=self.image_edit.text()
        number=int(self.spinBox.text())
        self.process_bar.setValue(0)
        self.process_bar.setMaximum(number)
        self.image_object.word=word
        self.image_object.max_number= number
        self.image_object.start()


    def process_bar_add(self,n):
        self.process_bar.setValue(n)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "图片爬取"))
        self.label_2.setText(_translate("MainWindow", "爬取图片关键字:"))
        self.label_3.setText(_translate("MainWindow", "爬取张数:"))
        self.label_4.setText(_translate("MainWindow", "下载进度:"))
        self.crawl_button.setText(_translate("MainWindow", "爬取"))
        self.menu_main.setTitle(_translate("MainWindow", "修改信息"))
        self.username.setText(_translate("MainWindow", "用户名"))
        self.password.setText(_translate("MainWindow", "密码"))


    def save_(self):
        if self.label_2.isVisible():
            if self.lineEdit.text() == "" or self.lineEdit_2.text()=="":
                QtWidgets.QMessageBox.warning(QtWidgets.QPushButton(),"Warning!","不能为空!")
            elif self.lineEdit.text()==self.lineEdit_2.text():
                self.cursor.execute("""update userlogin set password='%s'
                                where username='%s'  """ % (self.lineEdit_2.text(),self.usertext))
                self.conn.commit()
                QtWidgets.QMessageBox.information(QtWidgets.QPushButton(), "SUCESS!", "密码变更成功!")
                self.dialog.close()
            else:
                QtWidgets.QMessageBox.warning(QtWidgets.QPushButton(), "Warning!", "密码不一致!")
        elif self.lineEdit.text()=="":
            QtWidgets.QMessageBox.warning(QtWidgets.QPushButton(),"Warning!","不能为空!")
        else:
            self.cursor.execute("""update userlogin set username='%s'
                                            where username='%s'  """ % (self.lineEdit.text(), self.usertext))
            self.conn.commit()
            self.usertext=self.lineEdit.text()
            QtWidgets.QMessageBox.information(QtWidgets.QPushButton(), "SUCESS!", "用户名变更成功!")
            self.dialog.close()


    def processtrigger(self, q):
        self.dialog.resize(386, 258)
        self.lineEdit_2.setText("")
        self.lineEdit.setText("")
        if q.text() == "密码":
            self.font.setPointSize(30)
            self.label.setFont(self.font)
            self.label.setText("密码:")
            self.font.setPointSize(15)
            self.label_2.setFont(self.font)
            self.label_2.setText("确认密码:")
            self.label_2.setVisible(True)
            self.lineEdit_2.setVisible(True)
        else:
            self.font.setPointSize(20)
            self.label.setFont(self.font)
            self.label.setText("用户名:")
            self.label_2.setVisible(False)
            self.lineEdit_2.setVisible(False)

        self.Mw.close()
        self.dialog.show()
        self.dialog.exec()
        self.Mw.show()