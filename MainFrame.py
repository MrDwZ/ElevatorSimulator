from Ele import *


class MainFrame(Frame):
    _list = []

    def add_request(self, _from, _to, _text):
        self._list.append('from {} to {}'.format(_from, _to))
        _text.configure(state='normal')
        _text.delete("1.0", END)
        for item in self._list:
            _text.insert("1.0", item+"\n")
        _text.configure(state='disable')


    def __init__(self, master):

        Frame.__init__(self, master=master)
        input_form = Frame(master)
        input_form.pack()
        input_form.place(relx=0.05, rely=0.05, anchor=NW)

        from_label = Label(input_form, text="FROM:")
        from_label.pack(side=LEFT)

        from_entry = Entry(input_form)
        from_entry.pack(side=LEFT)

        to_label = Label(input_form, text="TO:")
        to_label.pack(side=LEFT)

        to_entry = Entry(input_form)
        to_entry.pack(side=LEFT)


        text = Text(master, width=40, height=40)
        text.pack()
        text.place(relx=0.05, rely=0.1, anchor=NW)
        text.config(state=DISABLED)

        confirm_button = Button(
            input_form,
            text="Confirm",
            command=lambda: self.add_request(
                int(from_entry.get()),
                int(to_entry.get()),
                text
            )
        )
        confirm_button.pack(side=LEFT)
