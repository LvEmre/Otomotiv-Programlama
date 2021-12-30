#Arayüzle çalışma örneği yazdırılan grafiğin rengini değiştirme -Github testi-
import sys
from PyQt5.QtWidgets import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("pokemon.csv", index_col=0)

class Pncr(QMainWindow):

    def __init__(ana):
        super().__init__()
        ana.title = 'Veri Görselleştirme'
        ana.setFixedWidth(500)
        ana.setFixedHeight(600)
        ana.Pncr2()
    
    def Pncr2(ana):
        button2 = QPushButton("Kaydet",ana)
        button2.setGeometry (10,100,100,50)
        button2.clicked.connect(ana.bas)

        button = QPushButton('Renk seçme', ana)
        button.setGeometry(10,10,100,50)
        button.clicked.connect(ana.on_click)
        ana.show()
    def bas(ana):
        plt.savefig('save_as_a_png.png')
    def on_click(ana):
        R= QColorDialog.getColor()
        renk = R.name()

        sns.displot(x='Attack', y='Defense',data=df,color = renk  )




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pncr()
    sys.exit(app.exec_())