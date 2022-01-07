from tkinter import Label, Tk

import time

app_window = Tk()



app_window.title("Dijital Saat")
app_window.geometry("400x150")
app_window.resizable(0,0)


clock3=int(time.strftime("%H"))

while (clock3>6 and clock3<18):
    text_font= ("Boulder", 68, 'bold')
    background = 'white'
    foreground= 'black'
    border_width = 25

    
    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
    
    label.grid(row=0, column=1)

    def digital_clock():
        time_live = time.strftime("%H:%M:%S")
        label.config(text=time_live)
        label.after(200, digital_clock)

    digital_clock()
    
    app_window.mainloop()
    

text_font= ("Boulder", 68, 'bold')
background = 'black'
foreground= 'white'
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)

label.grid(row=0, column=1)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)



digital_clock()


app_window.mainloop()