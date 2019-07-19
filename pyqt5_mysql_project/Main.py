from PyQt5.QtWidgets import QApplication,QDialog
from project import Ui_Dialog as pud
import sys
from PyQt5 import QtCore

class D(QDialog,pud):
    def __init__(self):
        super(D,self).__init__(None)
        self.setupUi(self)


if __name__=="__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)
    d=D()
    if d.isVisible():
        d.show()
    sys.exit(app.exec_())