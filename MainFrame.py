import Ele
from Tkinter import *
import Elevator


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
            Elevator.DOWN_TO[_to], Elevator.DOWN_FROM[_from] = True, True
        else:
            Elevator.UP_TO[_to], Elevator.UP_FROM[_from] = True, True

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

    def init_left_info(self):
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

        self.place(relx=0.5, rely=0.5, anchor=CENTER)

    def init_right_canvas(self, on_floor, offset):
        canvas = Canvas(self, width=285, height=570)
        canvas.grid(row=0, column=1)

        x, y = 20, 3
        width, height = 160, 100
        lower, upper = offset/5 * 5, (offset/5 + 1) * 5

        for i in xrange(0, 5):
            _floor = upper-i
            if _floor == on_floor:
                canvas.create_rectangle(x, y+i*height, x+width, y+(i+1)*height)
            else:
                canvas.create_rectangle(x, y+i*height, x+width, y+(i+1)*height, fill="black")

            text_x, text_y = x+width+20, (y+(i+0.5)*height)
            canvas.create_text(
                text_x, text_y,
                text=_floor,
                anchor="center",
                font=("Helvatica", 24)
            )

    def init_indication_mark(self, status):
        canvas = Canvas(self, width=150, height=60)
        canvas.grid(row=0, column=1, sticky=SW, padx=20)

        x, y = 10, 10
        width, height = 40, 40
        _text = ["IDLE", "UP", "DOWN"]

        for i in xrange(0, 3):
            if status == _text[i]:
                canvas.create_rectangle(x, y, x+width, y+height, fill="black")
            else:
                canvas.create_rectangle(x, y, x+width, y+height)

            canvas.create_text(
                x+width/2,
                y+height+10,
                text=_text[i],
                anchor="center",
                font=("Helvatica", "14")
            )
            x = x + width + 10

    def __init__(self, master):

        Frame.__init__(self, master=master)
        self.init_left_info()
        self.init_right_canvas(1, 1)
        self.init_indication_mark("IDLE")
