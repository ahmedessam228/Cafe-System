from tkinter import *
import sys
from tkinter import messagebox

sys.path.insert(0, "values")
sys.path.insert(0, "icons")
from colors import *
from fonts import *
from customtkinter import *
from PIL import Image


class LoginScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        loginFrame = CTkFrame(
            self.root,
            fg_color=darkBlue,
            bg_color=darkBlue,
            corner_radius=0,
        )

        titleLabel = CTkLabel(
            loginFrame,
            text="System Login",
            text_color=white,
            font=(lucida, 55),
            fg_color=transparent,
            bg_color=transparent,
            width=400,
            height=40,
        )
        titleLabel.grid(row=1, column=0, padx=50, pady=(50, 80))

        usernameFrame = CTkFrame(
            loginFrame,
            fg_color=darkBlue,
            bg_color=darkBlue,
            corner_radius=0,
            width=400,
        )

        usernameLabel = CTkLabel(
            usernameFrame,
            height=35,
            text="Username",
            text_color=white,
            font=(lucida, 24),
            fg_color=transparent,
            bg_color=transparent,
        )
        usernameLabel.grid(row=1, column=0)

        usernameEntry = CTkEntry(
            usernameFrame,
            width=400,
            height=50,
            corner_radius=10,
            border_width=0,
            fg_color=white,
            text_color=black,
            font=(normal, 20),
            placeholder_text="Username",
            placeholder_text_color=grey,
        )
        usernameEntry.grid(row=2, column=0, columnspan=80)

        usernameFrame.grid(row=2, column=0, padx=50, pady=40)

        passwordFrame = CTkFrame(
            loginFrame,
            fg_color=darkBlue,
            bg_color=darkBlue,
            corner_radius=0,
            width=400,
        )

        passwordLabel = CTkLabel(
            passwordFrame,
            text="Password",
            text_color=white,
            height=35,
            font=(lucida, 24),
            fg_color=transparent,
            bg_color=transparent,
        )
        passwordLabel.grid(row=1, column=0)

        passwordEntry = CTkEntry(
            passwordFrame,
            width=400,
            height=50,
            corner_radius=10,
            border_width=0,
            fg_color=white,
            text_color=black,
            font=(normal, 20),
            placeholder_text="Password",
            placeholder_text_color=grey,
            show='*'
        )
        passwordEntry.grid(row=2, column=0, columnspan=80)

        passwordFrame.grid(row=3, column=0, padx=50, pady=40)

        def toSelectionScreen():
            username = usernameEntry.get()
            password = passwordEntry.get()
            if username == "ahmed123" and password == "12345":
                self.root.destroy()
                from c_selection_screen import SelectionScreen
                SelectionScreen()
            else:
                messagebox.showerror("Error", "Invalid username or password")

        buttonLogin = CTkButton(
            loginFrame,
            width=150,
            height=50,
            text="Login",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 19),
            corner_radius=16,
            command=toSelectionScreen,
        )
        buttonLogin.grid(row=4, column=0, padx=175, pady=(40, screenHeight))

        loginFrame.place(x=0, y=0)

        logoFrame = CTkFrame(
            self.root,
            fg_color=transparent,
            bg_color=transparent,
            corner_radius=0,
        )

        logoLabel = CTkLabel(
            logoFrame,
            text="Cafe System",
            text_color=black,
            font=(lucida, 120),
            fg_color=transparent,
            bg_color=transparent,
            width=screenWidth - 500,
            height=180,
        )
        logoLabel.grid(row=1, column=0, pady=((screenHeight - 400) / 2, 0))

        cup = Image.open("icons/cup.png")
        icon = CTkImage(
            light_image=cup,
            size=(220, 220),
        )
        logo = CTkLabel(logoFrame, image=icon, text="")
        logo.grid(row=2, column=0, pady=(0, (screenHeight - 400) / 2))

        logoFrame.place(x=500, y=0)

        self.root.mainloop()
