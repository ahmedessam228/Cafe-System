from tkinter import *
from customtkinter import *
import sys

sys.path.insert(0, "values")
from fonts import *
from colors import *
from PIL import Image


class SplashScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Splash Screen")
        self.root.geometry("840x500+340+140")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        cup = Image.open("icons/cup.png")
        cup = cup.resize((80, 80))
        icon = CTkImage(light_image=cup, size=(80, 80))
        logo = CTkLabel(
            self.root,
            image=icon,
            bg_color=transparent,
            text="",
        )
        logo.place(x=388, y=250)

        label = Label(
            self.root,
            text="Cafe System",
            font=(lucida, 40),
            fg=black,
            bg=beige,
        )
        label.place(x=245, y=150)

        self.root.overrideredirect(True)

        def splashToLogin():
            self.root.destroy()
            from b_login_screen import LoginScreen

            LoginScreen()

        self.root.after(1000, splashToLogin)

        self.root.mainloop()


SplashScreen()
