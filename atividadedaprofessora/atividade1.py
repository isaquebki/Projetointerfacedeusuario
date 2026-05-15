from tkinter import *

class Aplicativo(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.msg = Label(self, text="Hello World")
        self.msg.pack()
        self.bye = Button(self, text="Bye", command=self.quit)
        self.bye.pack()
root = Tk()
app = Aplicativo(master=root)
app.mainloop()