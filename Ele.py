from Tkinter import *
from StartPage import *
from MainFrame import *

FLOOR_NUMBER = 0

class Ele(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.minsize(width=800, height=800)
        self.resizable(width=FALSE, height=FALSE)
        start_page = MainFrame(master=self)
