from MainFrame import *


MAX_FLOOR_NUMBER = 100
FLOOR_NUMBER = 1
UP_FROM = [0]*MAX_FLOOR_NUMBER
UP_TO = [0]*MAX_FLOOR_NUMBER
DOWN_FROM = [0]*MAX_FLOOR_NUMBER
DOWN_TO = [0]*MAX_FLOOR_NUMBER


class Ele(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.minsize(width=800, height=800)
        self.resizable(width=FALSE, height=FALSE)
        MainFrame(master=self)
