import Ele
from Tkinter import *


class MainFrame(Frame):
    info_list = []
    requests = []
    error_label = None
    from_entry = None
    to_entry = None

    @staticmethod
    def update_model(req):
        _from, _to = req
        if _from > _to:
            Ele.DOWN_TO[_to], Ele.DOWN_FROM[_from] = True, True
        else:
            Ele.UP_TO[_to], Ele.UP_FROM[_from] = True, True

    def update_ui(self, _text):
        _text.configure(state='normal')
        _text.delete("1.0", END)
        for item in self.info_list:
            _text.insert("1.0", item+"\n")
        _text.configure(state='disable')

    def add_request(self, _from, _to, _text):
        req = (_from, _to)

        if req not in self.requests:
            self.info_list.append('from {} to {}'.format(_from, _to))
            self.requests.append(req)

            self.update_model(req)
            self.update_ui(_text)
        else:
            self.error_label['text'] = "Request Duplicated."

        self.from_entry.delete(0, END)
        self.to_entry.delete(0, END)

    def __init__(self, master):

        Frame.__init__(self, master=master)

        input_form = Frame(self)
        Label(input_form, text="FROM:").grid(row=0, sticky=W)
        self.from_entry = Entry(input_form)
        self.from_entry.grid(row=0, column=1)

        Label(input_form, text="TO:").grid(row=1, sticky=W)
        self.to_entry = Entry(input_form)
        self.to_entry.grid(row=1, column=1)

        input_form.grid(row=1, column=0, pady=20, sticky=W)

        Button(
            input_form,
            text="Confirm",
            command=lambda: self.add_request(
                int(self.from_entry.get()),
                int(self.to_entry.get()),
                text
            )
        ).grid(row=2, column=0)

        self.error_label = Label(input_form, fg="red")
        self.error_label.grid(row=2, column=1)

        text = Text(self, width=40, height=40)
        text.grid(row=0, column=0)
        text.config(state=DISABLED, highlightbackground="black")

        self.place(relx=0.3, rely=0.5, anchor=CENTER)
