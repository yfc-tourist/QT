from PyQt5.QtCore import pyqtSignal,QThread,QDateTime,QTime,QDate

class TimeThread(QThread):
    t=pyqtSignal(str)

    def __init__(self):
        super(TimeThread,self).__init__(None)

    def run(self):
        while True:
            #print(QDateTime().currentDateTime().toString("yyyy MM/dd hh:mm:ss dddd"))
            self.t.emit(QDateTime().currentDateTime().toString(""" yyyy MM/dd 
   dddd
  hh:mm:ss"""))
            self.sleep(1)

