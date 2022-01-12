
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from todo import Pncr1
import sqlite3
from PyQt5.QtGui import QFont ,QPalette
from PyQt5.QtCore import QTimer, QTime, Qt
import subprocess
        
    
class MainWindow(QtWidgets.QMainWindow,QListWidget,QApplication,QLabel):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedWidth(795)
        self.setFixedHeight(395)
        
        #self.yok = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        #self.setWindowFlags(self.yok)
        
       

        self.kutu2 = QFrame(self)
        self.kutu2.setFrameShape(QFrame.StyledPanel)
        self.kutu2.setGeometry(50,10,320,270) 
        self.kutu2.setStyleSheet("background-color: White")

        self.kutu3 = QFrame(self)
        self.kutu3.setFrameShape(QFrame.StyledPanel)
        self.kutu3.setGeometry(5,5,785,385)
        self.kutu3.setStyleSheet("background:gray")
        
        self.kutu = QFrame(self)
        self.kutu.setFrameShape(QFrame.StyledPanel)
        self.kutu.setGeometry(440,40,320,100) 
        self.kutu.setStyleSheet("background-color: white")

        
        
        self.label = QLabel('Program açılıp kapanınca güncellenecektir.', self)
        self.label.setGeometry(60,0,300,50)
        self.label.show()
        
        self.label2 = QLabel('Butonların çalışması biraz uzun sürüyor bekleyiniz...', self)
        self.label2.setGeometry(60,265,250,50)
        self.label2.show()

        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(440, 170, 320, 200)

        fnt = QFont("Times New Roman", 30, QFont.Bold)

        self.lbl = QLabel(self)
        self.lbl.setGeometry(525,45,200,100)
        self.lbl.setFont(fnt)
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.label.show()

        self.kutu2.show()
        self.kutu.show()
        self.kutu3.show()
        
        self.But() 
        self.but2()
        self.but3()

        self.lbl.show()
        self.list()
        

        
    def But(haha):
        button = QPushButton("Liste ayarla",haha)
        button.setGeometry (60,250,100,20)
        button.clicked.connect(haha.bas)

    def but2(lol):  
        button2 = QPushButton("Hava Durumu",lol)
        button2.setGeometry (60,300,300,30)
        button2.setStyleSheet("background:white")
        button2.clicked.connect(lol.bas2)

    def but3(lel):   
        button3 = QPushButton("Yemek Önerisi",lel)
        button3.setGeometry (60,350,300,30)
        button3.setStyleSheet("background:white")
        button3.clicked.connect(lel.bas3)
        

    def list (yan):
        yan = QListWidget(yan)
        yan.setGeometry(60,40,300,200)
        yan.show()
        
        conn = sqlite3.connect('liste.db')
        c = conn.cursor()
        c.execute("SELECT * FROM todo_list")
        
        hu= c.fetchall()
        yan.clear()
        
        for i in range(len(hu)):
            item= QtWidgets.QListWidgetItem(hu[i][0])
            yan.addItem(item)


    def bas(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Pncr1()
        self.ui.habura(self.window)
        self.window.show()
        
    def bas2(hehe):
        subprocess.call('main.exe')

    def bas3(hehe):
        subprocess.call('yemeh.exe')

    def showTime(self):
        currentTime = QTime.currentTime()
        displayTxt = currentTime.toString('hh:mm:ss')
        self.lbl.setText(displayTxt)
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())