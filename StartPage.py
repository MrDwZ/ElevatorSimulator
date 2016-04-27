from Ele import *
from Tkinter import *


class StartPage(Frame):

    def delete_page(self):
        self.destroy()

    @staticmethod
    def set_floor_number(number):

        Ele.FLOOR_NUMBER = number
        print(FLOOR_NUMBER)

    def __init__(self, master):
        Frame.__init__(self, master=master)

        self.pack(expand=True, fill='both')

        Label(
            self,
            text="How many floors do you wanna have?",
            font=("Helvetica", 30)
        ).place(relx=0.5, rely=0.4, anchor=CENTER)

        form = Frame(self)
        e1 = Entry(form).pack(side=LEFT)

        Button(
            form,
            text="Confirm",
            command=lambda: self.set_floor_number(e1.get())
        ).pack(side=LEFT)

        Button(
            form,
            text="Cancel",
            command=self.delete_page
        ).pack(side=LEFT)

        form.place(relx=0.5, rely=0.5, anchor=CENTER)
