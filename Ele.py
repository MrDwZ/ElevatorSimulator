from MainFrame import *




class Ele(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.minsize(width=800, height=800)
        self.resizable(width=FALSE, height=FALSE)
        MainFrame(master=self)
