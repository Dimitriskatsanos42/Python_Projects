import os
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from turtle import width

class Notepad:
    root = Tk()

    Width = 600
    Height = 400
    TextArea = Text(root)
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    EditMenu = Menu(MenuBar, tearoff=0)
    HelpMenu = Menu(MenuBar, tearoff=0)

    ScrollBar = Scrollbar(TextArea)    
    file = None

    def __init__(self,**kwargs):
        
        try:
            self.root.wm_iconbitmap("Notepad.ioo")
        except:
            pass

        self.root.title("Untitled - Notepad")

        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        left = (screenWidth / 2) - (self.Width / 2)
        
        top = (screenHeight / 2) - (self.Height /2)        
        self.root.geometry('%dx%d+%d+%d' % (self.Width, self.Height, left, top))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.TextArea.grid(sticky = N + E + S + W)
        
        self.FileMenu.add_command(label="New", command=self.__newFile)
        
        self.FileMenu.add_command(label="Open", command=self.__openFile)
        
        self.FileMenu.add_command(label="Save", command=self.__saveFile)
        self.FileMenu.add_command(label="Exit", command=self.__exitApplication)
        self.MenuBar.add_cascade(label="File", menu=self.FileMenu)    
        
        self.EditMenu.add_command(label="Cut", command=self.__cut)            
    
        self.EditMenu.add_command(label="Copy", command=self.__copy)        
        
        self.EditMenu.add_command(label="Paste", command=self.__paste)        
        
        self.MenuBar.add_cascade(label="Edit", menu=self.EditMenu)    
        
        self.HelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.MenuBar.add_cascade(label="Help", menu=self.HelpMenu)
        self.root.config(menu=self.MenuBar)
        self.ScrollBar.pack(side=RIGHT,fill=Y)                
        
        self.ScrollBar.config(command=self.TextArea.yview)    
        self.TextArea.config(yscrollcommand=self.ScrollBar.set)
    
    def __exitApplication(self):
        self.root.destroy()

    def __showAbout(self):
        showinfo("notepad", "This os a notepad using thkinter module in python")
    
    def __openFile(self):

        self.__file= askopenfilename(defaultextension= ".txt", filetypes=[("all files", "*.*"), ("text documents", "*.txt")]) 

        if self.__file == " ":
           self.__file = None
        else:
            self.root.title(os.path.basename(self.__file) + " - Notepad")
            self.TextArea.delete(1.0, END)

            file = open(self.__file,"r")

            self.TextArea.insert(1.0,file.read())

            file.close()
    
    def __newFile(self):
        self.root.title("untitled - Notepad")
        self.__file = None
        self.TextArea.delete(1.0,END)

    def __saveFile(self):
        if self.__file == None:
            
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
            if self.__file == "":
                self.__file = None
            else:                
                file = open(self.__file,"w")
                file.write(self.TextArea.get(1.0,END))
                file.close()
                
                self.root.title(os.path.basename(self.__file) + " - Notepad")
        else:
            file = open(self.__file,"w")
            file.write(self.TextArea.get(1.0,END))
            file.close()
    
    def __cut(self):
        self.TextArea.event_generate("<<cut>>")
    
    def __copy(self):
        self.TextArea.event_generate("<<copy>>")
    
    def __paste(self):
        self.TextArea.event_generate("<<paste>>")
    
    def run(self):
        self.root.mainloop()
notepad = Notepad(width = 600, height =400)
notepad.run()