#!bin/bash
from tkinter import *

global summary
summary = "0"


def write_sym(value):
    summary = value


root = Tk()
root.title('simple')

master = Frame(root, width=300, height=350)
result = Label(master, text=summary)
b1 = Button(master, text='  1  ')
b2 = Button(master, text='  2  ')
b3 = Button(master, text='  3  ')
b4 = Button(master, text='  4  ')
b5 = Button(master, text='  5  ')
b6 = Button(master, text='  6  ')
b7 = Button(master, text='  7  ')
b8 = Button(master, text='  8  ')
b9 = Button(master, text='  9  ')
b0 = Button(master, text='  0  ')
add = Button(master, text="  +  ")
sub = Button(master, text="   -  ")
div = Button(master, text="   /  ")
mul = Button(master, text="   *  ")
dot = Button(master, text="  .   ")
equ = Button(master, text="  =  ")

result.grid(row=0, columnspan=4)
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)
b0.grid(row=4, column=0)
dot.grid(row=4, column=1)
add.grid(row=1, column=3)
sub.grid(row=2, column=3)
div.grid(row=3, column=3)
mul.grid(row=4, column=3)
equ.grid(row=4, column=2)
master.pack()
if __name__ == "__main__":
    mainloop()
