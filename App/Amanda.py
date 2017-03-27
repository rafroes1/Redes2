from Client.ClientTCP import ClientTCP
from tkinter import *

root = Tk()
root.title('Client: Amanda')
root.resizable(0, 0)
root.geometry('500x400+500+300')
main = ClientTCP('127.0.0.1', 9876, 'Amanda', root)
root.mainloop()