from tkinter import *
import sys

sys.path.insert(0, "values")
from colors import *
from fonts import *
from customtkinter import *
from PIL import Image


class SuccessScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Order Succes")
        self.root.geometry("840x500+340+140")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        self.root.overrideredirect(True)

        mainFrame = Frame(
            self.root,
            bg=beige,
        )

        cup = Image.open("icons\cup.png")
        cup = cup.resize((80, 80))
        icon = CTkImage(light_image=cup, size=(80, 80))
        logo = CTkLabel(
            self.root,
            image=icon,
            bg_color=transparent,
            text="",
        )
        logo.place(x=screenWidth - 100, y=20)

        successLabel = Label(
            mainFrame,
            text="Order Success",
            font=(lucida, 40),
            bg=beige,
        )
        successLabel.grid(row=0, column=0, pady=30)

        cup = Image.open("icons\checkmark.png")
        cup = cup.resize((80, 80))
        icon = CTkImage(light_image=cup, size=(80, 80))
        logo = CTkLabel(
            mainFrame,
            image=icon,
            bg_color=transparent,
            text="",
        )
        logo.grid(row=1, column=0)

        mainFrame.place(anchor="center", relx=0.5, rely=0.5)

        def toSelectionScreen():
            self.root.destroy()
            from c_selection_screen import SelectionScreen
            SelectionScreen()

        self.root.after(1000, toSelectionScreen)

        self.root.mainloop()
