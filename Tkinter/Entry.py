from tkinter import *
from Tkinter.Win import Win


class Entry_window:

    def __init__(self):
        self.master = Tk()
        self.e = Entry(self.master)
        self.e.pack()
        self.e.focus_set()
        self.b = Button(self.master, text="get", width=10, command=self.callback)
        self.b.pack()
        self.text = ""
        self.master.mainloop()

    def callback(self):
        x = self.e.get()
        self.master.destroy()
        Win(int(x), int(x))


