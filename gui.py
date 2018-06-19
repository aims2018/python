from tkinter import *
import tkinter as tk

root = tk.Tk()

def toHex(number):
    digits = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

    first = number//16
    second = number%16

    return(digits[first] + digits[second])

def listener(entry1,entry2,c,r1,g1,b1):
    temp = int(entry1.get())

    prime = 1

    counter = 2

    while(counter < temp):
        if(temp % counter == 0):
            prime = 0

        counter = counter + 1

    if (prime == 1):
        entry2.insert(0,"Prime")
    else:
        entry2.insert(0,"Composite")

    color = "#" + toHex(int(r1.get())) + toHex(int(g1.get())) + toHex(int(b1.get()))

    c.create_polygon(0,0,200,100,0,200,fill=color)




inputlabel =  Label(root,text="Input")
number = Entry(root)

outputlabel = Label(root,text="Output")
output = Entry(root)

canvas = Canvas(root,width=200,height=200)

redlabel = Label(root,text="Red")
red = Entry(root)
greenlabel = Label(root,text="Green")
green = Entry(root)
bluelabel = Label(root,text="Blue")
blue = Entry(root)

button = Button(root,text="Press Me",command=lambda e1=number,e2=output,c1=canvas,r=red,g=green,b=blue: listener(e1,e2,c1,r,g,b))

inputlabel.grid(row=0,column=0)
number.grid(row=0,column=1)
button.grid(row=1,column=0)
outputlabel.grid(row=2,column=0)
output.grid(row=2,column=1)
redlabel.grid(row=3,column=0)
red.grid(row=3,column=1)
greenlabel.grid(row=4,column=0)
green.grid(row=4,column=1)
bluelabel.grid(row=5,column=0)
blue.grid(row=5,column=1)
canvas.grid(row=6,column=0)

root.mainloop()