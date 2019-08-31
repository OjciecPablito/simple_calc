#!bin/bash
from tkinter import *


def write_sym(sym):
    result.insert(END, sym)


def calc():
    __result = result.get()
    ev = eval(__result)
    result.delete(0, END)
    if str(ev) == '0.0':
        result.insert(0, '0')
    else:
        result.insert(0, str(ev))


def clear():
    result.delete(0, END)


root = Tk()
root.title('simple')

master = Frame(root, width=300, height=350, bg='gray')
result = Entry(master, bg='#939393', border=0, fg='#FFF')
b1 = Button(master, text='1', command=lambda: write_sym('1'),
            width=7, height=2, bg='#004', fg='#FFF')

b2 = Button(master, text='2', command=lambda: write_sym('2'),
            width=7, height=2, bg='#004', fg='#FFF')

b3 = Button(master, text='3', command=lambda: write_sym('3'),
            width=7, height=2, bg='#004', fg='#FFF')

b4 = Button(master, text='4', command=lambda: write_sym('4'),
            width=7, height=2, bg='#004', fg='#FFF')

b5 = Button(master, text='5', command=lambda: write_sym('5'),
            width=7, height=2, bg='#004', fg='#FFF')

b6 = Button(master, text='6', command=lambda: write_sym('6'),
            width=7, height=2, bg='#004', fg='#FFF')

b7 = Button(master, text='7', command=lambda: write_sym('7'),
            width=7, height=2, bg='#004', fg='#FFF')

b8 = Button(master, text='8', command=lambda: write_sym('8'),
            width=7, height=2, bg='#004', fg='#FFF')

b9 = Button(master, text='9', command=lambda: write_sym('9'),
            width=7, height=2, bg='#004', fg='#FFF')

b0 = Button(master, text='0', command=lambda: write_sym('0'),
            width=7, height=2, bg='#004', fg='#FFF')

add = Button(master, text="+", command=lambda: write_sym('+'),
             width=7, height=2, bg='#004', fg='#FFF')

sub = Button(master, text="-", command=lambda: write_sym('-'),
             width=7, height=2, bg='#004', fg='#FFF')

div = Button(master, text="/", command=lambda: write_sym('/'),
             width=7, height=2, bg='#004', fg='#FFF')

mul = Button(master, text="*", command=lambda: write_sym('*'),
             width=7, height=2, bg='#004', fg='#FFF')

dot = Button(master, text=".", command=lambda: write_sym('.'),
             width=7, height=2, bg='#004', fg='#FFF')

equ = Button(master, text="=", command=lambda: calc(),
             width=7, height=2, bg='#004', fg='#FFF')
cls = Button(master, text="C", command=clear,
             width=7, height=2, bg="#004", fg="#FFF")


result.grid(row=0, columnspan=4, ipadx=50)
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
cls.grid(row=5, column=0)
master.pack()
if __name__ == "__main__":
    mainloop()
