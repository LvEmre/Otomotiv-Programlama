from tkinter import *
from tkinter import messagebox
from tkinter import font

pencere=Tk()

pencere.title("SarkanSepet")
pencere.geometry("500x500")

uygulama=Frame(pencere)
uygulama.grid()

lahmacun=49.90
cantık=22.90
pizza=58
mantı=31.69
wellington=2999.99
toplam=0
    
def heasp():
    var=messagebox.showinfo("Sepet", "Sepete Eklendi")
    
def sepet():
    var=messagebox.showinfo("Sipariş", "Siparişiniz Alındı")
    
    
button_background='wheat'
text_font=("Boulder", 10, 'bold')
lastbutton_background='indian red'
lastbutton_textfont=("Boulder", 20, 'bold')

button1=Button(uygulama, text="Lahmacun\n49,90 TL", width=12, height=2, command=heasp, background=button_background, font=text_font)
button1.grid(padx=11, pady=11)
    
button2=Button(uygulama, text="Cantık\n22,90 TL", width=12, height=2, command=heasp, background=button_background, font=text_font)
button2.grid(padx=11, pady=11)

button3=Button(uygulama, text="Pizza\n58,00 TL", width=12, height=2, command=heasp, background=button_background, font=text_font)
button3.grid(padx=11, pady=11)

button4=Button(uygulama, text="Mantı\n31,69 TL", width=12, height=2, command=heasp, background=button_background, font=text_font)
button4.grid(padx=11, pady=11)

button5=Button(uygulama, text="Beef Wellington\n2999,99 TL", width=12, height=2, command=heasp, background=button_background, font=text_font)
button5.grid(padx=11, pady=11)

button6=Button(uygulama, text="Siparişi\nTamamla", width=12, height=3, command=sepet, background=lastbutton_background, font=lastbutton_textfont)
button6.grid(padx=150, pady=26)

pencere.mainloop()


#Toplam fiyat sorununu çözemedim