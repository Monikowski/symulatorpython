from tkinter import *
import pickle


class Entry_load:

    def __init__(self, caller):
        self.caller = caller
        self.master = Tk()
        self.e = Entry(self.master)
        self.e.pack()
        self.e.focus_set()
        self.b = Button(self.master, text="get", width=10, command=self.callback)
        self.b.pack()
        self.text = ""
        self.master.mainloop()

    def callback(self):
        txt = self.e.get()
        with open(txt + ".pkl", 'rb') as infile:
            x = pickle.load(infile)
            y = pickle.load(infile)
            org_board = pickle.load(infile)
            org_list = pickle.load(infile)
            infile.close()
            self.caller.root.destroy()
            self.master.destroy()
        self.caller.new(x, y, org_board, org_list)
