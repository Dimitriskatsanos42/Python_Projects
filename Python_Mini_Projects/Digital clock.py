from tkinter import * 
from tkinter.ttk import *
  
from time import strftime
  
root = Tk()
root.title('Clock')


def time():
    string = strftime('%H:%M:%S %p')
    bl.config(text = string)
    bl.after(1000, time)
  
bl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'cornflowerblue', 
            foreground = 'azure1')
  
bl.pack(anchor = 'center')
time()
  
mainloop()
