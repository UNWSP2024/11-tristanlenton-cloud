import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.button = tkinter.Button(self.window, text="Show Info", command=self.showInfo)
        self.quitButton = tkinter.Button(self.window, text="Quit", command=self.window.destroy)
        self.button.pack()
        self.quitButton.pack()
        tkinter.mainloop()
    def showInfo(self):
        tkinter.messagebox.showinfo("Name: Tristan Lenton", "Address: 123 Main Street, Buffalo MN")
myGUI = GUI()
