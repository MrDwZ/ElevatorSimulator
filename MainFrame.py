import Ele
from Tkinter import *
import Elevator


class MainFrame(Frame):
    info_list = []
    error_label = None
    from_entry = None
    to_entry = None
    text = None
    indicator = None
    main_canvas = None

    def add_request(self, _from, _to):
        req = (_from, _to)

        if req not in Elevator.REQUESTS:
            self.info_list.append('from {} to {}'.format(_from, _to))
            Elevator.REQUESTS.append(req)
        else:
            self.error_label['text'] = "Request Duplicated."

        self.from_entry.delete(0, END)
        self.to_entry.delete(0, END)

        self.text.configure(state='normal')
        self.text.delete("1.0", END)
        for item in self.info_list:
            self.text.insert("1.0", item+"\n")
        self.text.configure(state='disable')
        Elevator.call(_from, _to)

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
            )
        ).grid(row=2, column=0)

        self.error_label = Label(input_form, fg="red")
        self.error_label.grid(row=2, column=1)

        self.text = Text(self, width=40, height=40)
        self.text.grid(row=0, column=0)
        self.text.config(state=DISABLED, highlightbackground="black")

        self.place(relx=0.5, rely=0.5, anchor=CENTER)

    def set_right_canvas(self, on_floor):
        if self.main_canvas is None:
            self.main_canvas = Canvas(self, width=285, height=570)
            self.main_canvas.grid(row=0, column=1)
        else:
            self.main_canvas.delete("all")

        x, y = 20, 3
        width, height = 160, 100
        offset = on_floor / 5 * 5
        lower, upper = offset/5 * 5, (offset/5 + 1) * 5

        for i in xrange(0, 5):
            _floor = upper-i
            if _floor == Elevator.CURRENT_FLOOR:
                self.main_canvas.create_rectangle(x, y+i*height, x+width, y+(i+1)*height)
            else:
                self.main_canvas.create_rectangle(x, y+i*height, x+width, y+(i+1)*height, fill="black")

            text_x, text_y = x+width+20, (y+(i+0.5)*height)
            self.main_canvas.create_text(
                text_x, text_y,
                text=_floor,
                anchor="center",
                font=("Helvatica", 24)
            )

    def set_indicator(self, status):

        if self.indicator is None:
            self.indicator = Canvas(self, width=150, height=60)
            self.indicator.grid(row=0, column=1, sticky=SW, padx=20)
        else:
            self.indicator.delete("all")

        x, y = 10, 10
        width, height = 40, 40
        _text = [Elevator.IDLE, Elevator.UP, Elevator.DOWN]
        _str = ["IDLE", "UP", "DOWN"]

        for i in xrange(0, 3):
            if status == _text[i]:
                self.indicator.create_rectangle(x, y, x+width, y+height, fill="black")
            else:
                self.indicator.create_rectangle(x, y, x+width, y+height)

            self.indicator.create_text(
                x+width/2,
                y+height+10,
                text=_str[i],
                anchor="center",
                font=("Helvatica", "14")
            )
            x = x + width + 10

    def next_scenario(self):

        # Decide the elevator's next direction when it is IDLE
        if len(Elevator.REQUESTS) == 0:
            Elevator.DIRECTION = Elevator.IDLE
        elif Elevator.DIRECTION == Elevator.IDLE:
            if Elevator.has_from_request_from_upper_floor():
                Elevator.DIRECTION = Elevator.UP
            elif Elevator.has_from_request_from_lower_floor():
                Elevator.DIRECTION = Elevator.DOWN
            elif Elevator.has_to_request_from_upper_floor():
                Elevator.DIRECTION = Elevator.UP
            elif Elevator.has_to_request_from_lower_floor():
                Elevator.DIRECTION = Elevator.DOWN

        Elevator.move()

        # Detect if there is anyone wanna embark the elevator on current floor
        if any(req[0] == Elevator.CURRENT_FLOOR for req in Elevator.REQUESTS):
            Elevator.DIRECTION = Elevator.IDLE

        # Detect if there is anyone wanna disembark the elevator on current floor
        if any(req[1] == Elevator.CURRENT_FLOOR for req in Elevator.REQUESTS):
            Elevator.REQUESTS = \
                [req for req in Elevator.REQUESTS if req[1] != Elevator.CURRENT_FLOOR]
            Elevator.DIRECTION = Elevator.IDLE

        self.set_indicator(Elevator.DIRECTION)
        self.set_right_canvas(Elevator.CURRENT_FLOOR)
        self.after(Ele.REFRESH_RATE, lambda: self.next_scenario())

    def __init__(self, master):

        Frame.__init__(self, master=master)
        self.init_left_info()
        self.set_right_canvas(1)
        self.set_indicator(Elevator.IDLE)
        self.after(Ele.REFRESH_RATE, lambda: self.next_scenario())
