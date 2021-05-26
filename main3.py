import calendar
from tkinter import *


tk = Tk()
tk.title("Calendar")


#Button Function
def myFunc():
    month_ = int(month.get())
    year_ = int(year.get())
    cal = calendar.month(year_, month_)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)
#Button Function


#Texts
label1 = Label(tk, text="Month\n-------",fg="red")
label1.grid(row=0, column=0)

label2 = Label(tk, text="Year\n-----",fg="red")
label2.grid(row=0, column=1)
#Texts

#Spinboxes
month = Spinbox(tk, from_=1, to=12, width=8,fg="blue")
month.grid(row=1, column=0, padx=5)

year = Spinbox(tk, from_=1900, to=2300, width=10,fg="blue")
year.grid(row=1, column=1, padx=10)
#Spinboxes

#Start Button
button = Button(tk, text="Go", command=myFunc)
button.grid(row=1, column=2, padx=10)
#Start Button

#Show Calendar Area
textfield = Text(tk, width=20, height=10, fg="black")
textfield.grid(row=2, columnspan=2)
#Show Calendar Area


tk.mainloop()
