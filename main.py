from Global import *
import tkinter
import Layout


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.resolution = (400, 350)
        self.title("Pizza Cutter")
        self.iconbitmap(fix_path("./Images/Icon.ico"))
        self.geometry("{}x{}".format(*self.resolution))
        self.resizable(False, False)
        self.main_frame = Layout.MainFrame(self)
        self.main_frame.pack(expand=True, fill="both")
        self.mainloop()


if __name__ == "__main__":
    Window()
