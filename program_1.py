import tkinter

class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Python GUI")
        self.label = tkinter.Label(self.window, text="AGAIN! -Herb Brooks")
        self.label.pack()
        tkinter.mainloop()
myGUI = GUI()
myGUI.window.mainloop()