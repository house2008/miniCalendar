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
"""
from tkinter import *
import calendar

win = Tk()
win.title("GUI Calendar")


def te():
    year_str = year.get()
    month_str = month.get()
    year_int = int(year_str)
    month_int = int(month_str)
    cal = calendar.month(year_int, month_int)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)


label1 = Label(win, text="{Year} ")
label1.grid(row=0, column=0)
label1 = Label(win, text="{Month} ")
label1.grid(row=0, column=1)

year = Spinbox(win, from_=1947, to=2150, width=24)
year.grid(row=1, column=0, padx=16)
month = Spinbox(win, from_=1, to=12, width=3)
month.grid(row=1, column=1)

button = Button(win, text="{GO}", command=te)
button.grid(row=1, column=2)

textfield = Text(win, height=10, width=30, foreground="brown")
textfield.grid(row=3, columnspan=3)

win.mainloop()
from tkinter import *
import calendar

win = Tk()
win.title("GUI Calendar")


def show_calendar():
    year_str = year_spin.get()
    month_str = month_spin.get()
    year_int = int(year_str)
    month_int = int(month_str)
    cal = calendar.month(year_int, month_int)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)


# 标签
label_year = Label(win, text="Year")
label_year.grid(row=0, column=0)
label_month = Label(win, text="Month")
label_month.grid(row=0, column=1)

# 输入框
year_spin = Spinbox(win, from_=1947, to=2150, width=24)
year_spin.grid(row=1, column=0, padx=16)
month_spin = Spinbox(win, from_=1, to=12, width=3)
month_spin.grid(row=1, column=1)

# 按钮
button = Button(win, text="GO", command=show_calendar)
button.grid(row=1, column=2)

# 文本显示区
textfield = Text(win, height=10, width=30, foreground="brown")
textfield.grid(row=3, columnspan=3)

win.mainloop()
"""