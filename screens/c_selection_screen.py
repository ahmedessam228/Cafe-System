from tkinter import *
import sys

sys.path.insert(0, "values")
from colors import *
from fonts import *
from customtkinter import *
from tkinter import ttk
from PIL import Image


class SelectionScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Select Order Type")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        cup = Image.open("icons\cup.png")
        cup = cup.resize((80, 80))
        icon = CTkImage(light_image=cup, size=(80, 80))
        logo = CTkLabel(self.root, image=icon, bg_color=transparent, text="")
        logo.place(x=screenWidth - 100, y=20)

        titleLabel = Label(
            self.root,
            font=(lucida, 40),
            text="Select Order Type",
            bg=beige,
        )
        titleLabel.place(x=10, y=30)

        buttonsFrame = CTkFrame(
            self.root,
            bg_color=transparent,
            fg_color=transparent,
        )

        def toMenuCafe():
            self.root.destroy()
            from d_menu_screen import MenuScreen
            MenuScreen(selection="cafe")

        buttonCafe = CTkButton(
            buttonsFrame,
            width=500,
            height=250,
            fg_color=white,
            text_color=black,
            border_width=5,
            corner_radius=30,
            border_color=darkBlue,
            text="Cafe",
            font=(lucida, 48),
            hover_color=cafe,
            command=toMenuCafe,
        )
        buttonCafe.grid(row=0, column=0, padx=(0, 100))

        def toMenuTakeAway():
            self.root.destroy()
            from d_menu_screen import MenuScreen
            MenuScreen(selection="takeaway")

        buttonTakeAway = CTkButton(
            buttonsFrame,
            width=500,
            height=250,
            fg_color=white,
            text_color=black,
            border_width=5,
            corner_radius=30,
            border_color=darkBlue,
            text="Take Away",
            font=(lucida, 48),
            hover_color=cafe,
            command=toMenuTakeAway,
        )
        buttonTakeAway.grid(row=0, column=1, padx=(100, 50), pady=50)

        buttonsFrame.place(anchor="center", relx=0.5, rely=0.5)

        self.root.mainloop()
# SelectionScreen()
