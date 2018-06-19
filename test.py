from tkinter import *
import tkinter as tk

root = tk.Tk()

options = [];

counter = 0

while (counter < 256):
    options += [counter]

    counter += 1

def toHex(number):
    digits=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

    first = number//16
    second = number%16

    return(digits[first] + digits[second])

def draw1(var1,var2,var3,c):
    color = "#" + toHex(int(var1.get())) + toHex(int(var2.get())) + toHex(int(var3.get()))

    c.create_oval(50,50,100,100,fill=color)

    return(1)

redvar = StringVar(root)

red = OptionMenu(root,redvar,*options)

greenvar = StringVar(root)

green = OptionMenu(root,greenvar,*options)

bluevar = StringVar(root)

blue = OptionMenu(root,bluevar,*options)

canvas = Canvas(root,width=100,height=100)

draw = Button(root,text="Draw",command=lambda r=redvar,g=greenvar,b=bluevar,c=canvas: draw1(r,g,b,canvas))

red.grid(row=0,column=0)
green.grid(row=1,column=0)
blue.grid(row=2,column=0)
draw.grid(row=3,column=0)
canvas.grid(row=4,column=0)

root.mainloop()