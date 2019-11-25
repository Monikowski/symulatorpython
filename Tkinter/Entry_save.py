from tkinter import *
import pickle


class Entry_save:

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
        with open(txt + ".pkl", 'wb') as outfile:
            pickle.dump(self.caller.world.width, outfile, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.caller.world.height, outfile, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.caller.world.organisms_board, outfile, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.caller.world.organisms_list, outfile, pickle.HIGHEST_PROTOCOL)
            outfile.close()
        self.master.destroy()
