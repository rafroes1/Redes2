from Client.ClientTCP import ClientTCP
from tkinter import *

root = Tk()
root.title('Client')
root.resizable(0, 0)
root.geometry('500x400+500+300')

label = Label(root, text="Username")
label.grid(row=0, column=0)

entry = Entry(root, bd=5)
entry.grid(row=0, column=1)

def sysout():
    nick = entry.get()
    entry.grid_remove()
    label.grid_remove()
    buttom.grid_remove()
    start(nick)

buttom = Button(root, text="go", width=10, command=sysout)
buttom.grid(row=1, column=0, columnspan=2)

def start(nick):
    ###-------------SET IP HERE---------------###
    main = ClientTCP("localhost", 6789, nick, root)

root.mainloop()