from Server.ServerTCP import ServerTCP
from tkinter import *

root = Tk()
root.title('Server')
root.resizable(0, 0)
root.geometry('180x200+1200+400')
main = ServerTCP(root)
root.mainloop()
