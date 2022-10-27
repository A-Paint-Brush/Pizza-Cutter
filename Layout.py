import tkinter
import tkinter.ttk
import Canvas


class MainFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.canvas = tkinter.Canvas(self)
        self.canvas.pack()
        self.renderer = None
        tkinter.ttk.Separator(self).pack(pady=(10, 0), fill="x")
        tkinter.Label(self, text="Enter a number below to cut the pizza.").pack()
        self.validate_cmd = (self.register(self.update_canvas), "%P")
        self.entry = tkinter.Spinbox(self,
                                     from_=1,
                                     to=360,
                                     validate="key",
                                     validatecommand=self.validate_cmd,
                                     state="disabled")
        self.entry.pack()
        self.entry.focus()
        self.entry.icursor("end")  # Automatically focus the spinbox widget and place the text caret at the end.
        self.canvas.bind("<Configure>", self.init_canvas)  # This will be triggered once the window loads.

    def init_canvas(self, event):
        self.renderer = Canvas.Renderer(self.canvas, (event.width, event.height))
        self.renderer.update_canvas(1)  # Initialize the pizza with no cuts.
        self.entry.config(state="normal")

    def update_canvas(self, new_value):
        if self.renderer is None:
            return True
        if (new_value.isdigit() and int(new_value) <= 360) or (not new_value):
            # The above statement blocks non-number characters and values bigger than 360.
            if int(new_value or 0) == 0 and len(new_value) > 1:
                # Block strings that evaluate to zero, but are made of more than one "0" characters. e.g. "00000"
                self.bell()
                return False
            if int(new_value or 1) >= 1:
                # Empty strings are treated as the numeric value '1'.
                # If value is the number zero, it is allowed into the textbox, but update_canvas() is not called.
                self.renderer.update_canvas(int(new_value or 1))
            return True
        else:
            self.bell()
            return False
