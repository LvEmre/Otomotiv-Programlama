from tkinter import *

def yazı_ekleme():
    task = eklenenler.get()
    if task != "":
        lb.insert(END, task)
   

def yazı_silme():
    lb.delete(ANCHOR)

# pencerenin özellikleri:
pencere = Tk()
pencere.geometry('350x400+350+200')
pencere.title('Yapılacaklar Listem')
pencere.config(bg='#cccccc')
pencere.resizable(width=False, height=False)
frame = Frame(pencere)
frame.pack(pady=10)

# liste kutusu özellikleri:
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#0c1404',
    highlightthickness=0,
    selectbackground='#7f7f7f',
    activestyle="none",)

lb.pack(side=LEFT, fill=BOTH)

# listenin içindeki yazılar:
listenin_içindekiler = [
    '9.30 Matematik Sınavı',
    '12.00 spor',
    '14.00 Okul toplantısı',
    '16.00 Sınıf Yemeği', ]

for item in listenin_içindekiler:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

eklenenler = Entry(
    pencere,
    font=('times', 24))

eklenenler.pack(pady=20)

button_frame = Frame(pencere)
button_frame.pack(pady=20)

# butonların özellikleri:
ekleme_butonu = Button(
    button_frame,
    text='Listeye Ekle',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=yazı_ekleme)

ekleme_butonu.pack(fill=BOTH, expand=True, side=LEFT)

silme_butonu = Button(
    button_frame,
    text='Listeden Sil',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=yazı_silme)

silme_butonu.pack(fill=BOTH, expand=True, side=LEFT)


pencere.mainloop()