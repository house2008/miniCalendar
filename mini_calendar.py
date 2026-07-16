from tkinter import *
import calendar

win = Tk()
win.title("A graphic calendar")

def text():
    ys = year.get()
    ms = month.get()
    yi = int(ys)
    mi = int(ms)
    cal = calendar.month(yi,mi)
    textfield.delete(0.0,END)
    textfield.insert(INSERT,cal)

label1 = Label(win,text='{Year}')
label1.grid(row=0,column=0)
label1 = Label(win,text='{Month}')
label1.grid(row=0,column=1)

year = Spinbox(win,from_=1947,to=2150,width=24)
year.grid(row=1,column=0,padx=16)
month = Spinbox(win,from_=1,to=12,width=3)
month.grid(row=1,column=1)

button = Button(win,text = '{GO}',command=text)
button.grid(row=1,column=2)

textfield = Text(win,height=10,width=30,foreground='brown')
textfield.grid(row=3,columnspan=3)

win.mainloop()
