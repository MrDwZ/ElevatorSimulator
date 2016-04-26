from Ele import *


class StartPage(Frame):

    def delete_page(self):
        self.destroy()

    @staticmethod
    def set_floor_number(number):

        Ele.FLOOR_NUMBER = number
        print(FLOOR_NUMBER)

    def __init__(self, master):
        Frame.__init__(Frame(self), master=master)

        self.pack(expand=True, fill='both')
        w = Label(self, text="How many floors do you wanna have?", font=("Helvetica", 30))
        w.place(relx=0.5, rely=0.4, anchor=CENTER)

        form = Frame(self)
        e1 = Entry(form)
        e1.pack(side=LEFT)
        confirm_button = Button(form, text="Confirm", command=lambda: self.set_floor_number(e1.get()))
        confirm_button.pack(side=LEFT)
        cancel_button = Button(form, text="Cancel", command=self.delete_page)
        cancel_button.pack(side=LEFT)
        form.place(relx=0.5, rely=0.5, anchor=CENTER)
