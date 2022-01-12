from PyQt5 import QtCore, QtWidgets
import sqlite3

conn = sqlite3.connect('liste.db')

c = conn.cursor()


c.execute("""CREATE TABLE if not exists todo_list(
    list_item text)
    """)


conn.commit()


conn.close()


class Pncr1(object):
    def habura(self, AnaPncr):
        AnaPncr.setObjectName("Yapılacaklar_listesi")
        AnaPncr.setFixedWidth(520)
        AnaPncr.setFixedHeight(350)
        self.centralwidget = QtWidgets.QWidget(AnaPncr)
        self.centralwidget.setObjectName("centralwidget")
        self.ekleme = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.ekle())
        self.ekleme.setGeometry(QtCore.QRect(10, 50, 120, 30))
        self.ekleme.setObjectName("ekleme")
        self.teksil = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.kaldır())
        self.teksil.setGeometry(QtCore.QRect(140, 50, 140, 30))
        self.teksil.setObjectName("teksil")
        self.toplusil = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.sil())
        self.toplusil.setGeometry(QtCore.QRect(290, 50, 100, 30))
        self.toplusil.setObjectName("toplusil")
        self.ekleme_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ekleme_edit.setGeometry(QtCore.QRect(10, 10, 500, 30))
        self.ekleme_edit.setObjectName("ekleme_edit")
        self.liste = QtWidgets.QListWidget(self.centralwidget)
        self.liste.setGeometry(QtCore.QRect(10, 90, 500, 230))
        self.liste.setObjectName("liste")
        self.savedb = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.save_it())
        self.savedb.setGeometry(QtCore.QRect(400, 50, 111, 31))
        self.savedb.setObjectName("savedb")
        AnaPncr.setCentralWidget(self.centralwidget)
        self.menu = QtWidgets.QMenuBar(AnaPncr)
        self.menu.setGeometry(QtCore.QRect(0, 0, 405, 20))

        AnaPncr.setMenuBar(self.menu)
        self.statusbar = QtWidgets.QStatusBar(AnaPncr)
        self.statusbar.setObjectName("statusbar")
        AnaPncr.setStatusBar(self.statusbar)

        self.retranslateUi(AnaPncr)
        QtCore.QMetaObject.connectSlotsByName(AnaPncr)
        self.gayıt()
    def gayıt(self):
        
        conn = sqlite3.connect('liste.db')
        
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()


        
        conn.commit()

        
        conn.close()

        
        for record in records:
            self.liste.addItem(str(record[0]))
    
    
    def ekle(self):
        
        item = self.ekleme_edit.text()
        self.liste.addItem(item)
        self.ekleme_edit.setText("")

    
    def kaldır(self):
        
        clicked = self.liste.currentRow()
        self.liste.takeItem(clicked)

    
    def sil(self):
        self.liste.clear()
    def save_it(self):
        conn = sqlite3.connect('liste.db')
        c = conn.cursor()
        c.execute('DELETE FROM todo_list;',)
        items = []
        for index in range(self.liste.count()):
            items.append(self.liste.item(index))

        for item in items:
            c.execute("INSERT INTO todo_list VALUES (:item)",
                {
                    'item': item.text(),
                })
          
        conn.commit()
        conn.close()   
    def retranslateUi(self, AnaPncr):
        ceviri = QtCore.QCoreApplication.translate
        AnaPncr.setWindowTitle(ceviri("Ana Ekran", "Alınacaklar listesi"))
        self.ekleme.setText(ceviri("Ana Ekran", "Ekle"))
        self.teksil.setText(ceviri("Ana Ekran", "Çıkar"))
        self.toplusil.setText(ceviri("Ana Ekran", "Temizle"))
        self.savedb.setText(ceviri("Ama Ekram", "Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnaPncr = QtWidgets.QMainWindow()
    ui = Pncr1()
    ui.habura(AnaPncr)
    AnaPncr.show()
    sys.exit(app.exec_())