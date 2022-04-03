from tkinter import *
from random import randint
root = Tk()
lab = Label(root)
lab.pack()


a = 0


def update():
    global a
    a += 1
    lab['text'] = a
    root.after(1000, update) # run itself again after 1000 ms

# run first time
update()

root.mainloop()