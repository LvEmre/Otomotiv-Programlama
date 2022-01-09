
from tkinter import *
from tkinter.ttk import *
import numpy as np
import pandas as pd
import random
import tkinter as tk


ana_pencere = Tk()
ana_pencere.geometry("600x200")
ana_pencere.config(bg='#cccccc')
ana_pencere.title("")
# yemek ve tatlı pencerelerinin özellikleri ve fonksiyonları:
# yemek penceresi:
def yemek_penceresi():
	
    csv_dosyası = pd.read_csv("yemek listesi.csv")
    csv_dosyası = np.array(csv_dosyası)

    yemekler=[]
    for i in csv_dosyası:
        yemekler.append((i[1],i[2]))
    
    def öneri_fonksiyonu():

        yazı.delete('1.0', tk.END)
        r = random.choice(yemekler)
        msg = r[0] +"(" + r[1] + ")"
        yazı.insert(tk.END,msg)

    # Pencerenin özellikleri:
    pencere = tk.Tk()
    pencere.geometry("600x200")
    pencere.config(bg="#cccccc")
    pencere.title('Yemek önerileri')


    # Butonlar ve özellikleri:
    a1 = tk.Label(pencere,text="Önerilerimiz için butona tıklayın. (Farklı öneriler için tıklamaya devam et)",font=("Times",13),fg="Black",bg="White")
    a1.place(x=30,y=10)

    b1 = tk.Button(pencere,text="Buraya tıkla",font=("Times",15),bg="#8B9A46",fg="white",command=öneri_fonksiyonu)
    b1.place(x=200,y=60)

    yazı = tk.Text(pencere,width=50,height=1,font=("Times",15))
    yazı.place(x=15,y=120) 


# tatlı penceresi:
def tatlı_penceresi():
	
    csv_dosyası = pd.read_csv("tatlı listesi.csv")
    csv_dosyası = np.array(csv_dosyası)

    yemekler=[]
    for i in csv_dosyası:
        yemekler.append((i[1],i[2]))
    
    def öneri_fonksiyonu():

        yazı.delete('1.0', tk.END)
        r = random.choice(yemekler)
        msg = r[0] +"(" + r[1] + ")"
        yazı.insert(tk.END,msg)



    # Pencerenin özellikleri:
    pencere = tk.Tk()
    pencere.geometry("600x200")
    pencere.config(bg="#cccccc")
    pencere.title('Tatlı önerileri')


    # Butonlar ve özellikleri:
    a1 = tk.Label(pencere,text="Önerilerimiz için butona tıklayın. (Farklı öneriler için tıklamaya devam et)",font=("Times",13),fg="Black",bg="White")
    a1.place(x=30,y=10)

    b1 = tk.Button(pencere,text="Buraya tıkla",font=("Times",15),bg="#8B9A46",fg="white",command=öneri_fonksiyonu)
    b1.place(x=200,y=60)

    yazı = tk.Text(pencere,width=50,height=1,font=("Times",15))
    yazı.place(x=15,y=120) 



# butonların özellikleri(FONT SİZE DEĞİŞTİREMEDİM, height KOMUTU ÇALIŞMIYO)

label = Label(ana_pencere,text ="Ne önermemizi istersin? Canın tatlı mı istiyor yoksa yemek mi?",font=("Times",15) )

label.pack(pady = 10,)

btn = Button(ana_pencere,
			text ="Bana yemek öner.",command = yemek_penceresi,width=40)
btn.pack(pady = 10)


btn2 = Button(ana_pencere,
			text ="Bana tatlı öner.",command = tatlı_penceresi,width=40)
btn2.pack(pady = 10)


mainloop()
