from tkinter import *
import sys

sys.path.insert(0, "values")
sys.path.insert(0, "classes")
from colors import *
from fonts import *
from client import *
from customtkinter import *
from PIL import Image


class CashScreen:
    def __init__(self, price, selection, client, orders):
        self.root = Tk()
        self.root.title("Cash Calculate")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        self.remaining = 0
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        titleLabel = Label(
            self.root,
            font=(lucida, 40),
            text="Cash Calculate",
            bg=beige,
        )
        titleLabel.place(x=10, y=30)

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

        mainFrame = CTkFrame(
            self.root,
            fg_color=darkBlue,
            bg_color=transparent,
            corner_radius=50,
        )

        priceFrame = CTkFrame(
            mainFrame,
            fg_color=transparent,
            bg_color=transparent,
            corner_radius=20,
        )

        priceTemp = CTkLabel(
            priceFrame,
            text="",
            width=550,
            height=0,
            bg_color=transparent,
            fg_color=transparent,
        )
        priceTemp.grid(row=0, column=1, columnspan=80)

        priceLabel = CTkLabel(
            priceFrame,
            text="Price :",
            text_color=white,
            font=(lucida, 22),
            fg_color=transparent,
            bg_color=transparent,
        )
        priceLabel.grid(row=0, column=1)

        priceValue = CTkLabel(
            priceFrame,
            text=str(price) + " ",
            text_color=white,
            font=(lucida, 22),
            fg_color=transparent,
            bg_color=transparent,
        )
        priceValue.grid(row=0, column=80)

        priceFrame.grid(row=1, column=1, pady=(40, 20), padx=30)

        paidFrame = CTkFrame(
            mainFrame,
            fg_color=transparent,
            bg_color=transparent,
            corner_radius=20,
        )

        paidLabel = CTkLabel(
            paidFrame,
            text="Paid",
            text_color=white,
            font=(lucida, 22),
            fg_color=transparent,
            bg_color=transparent,
        )
        paidLabel.grid(row=1, column=0)

        paidFrame.grid(row=2, column=1, pady=20, padx=30)

        discountFrame = CTkFrame(
            mainFrame,
            fg_color=transparent,
            bg_color=transparent,
            corner_radius=20,
        )

        discountLabel = CTkLabel(
            discountFrame,
            text="Discount",
            text_color=white,
            font=(lucida, 22),
            fg_color=transparent,
            bg_color=transparent,
        )
        discountLabel.grid(row=1, column=0)

        discountFrame.grid(row=3, column=1, pady=20, padx=30)

        remainingFrame = CTkFrame(
            mainFrame,
            fg_color=transparent,
            bg_color=transparent,
            corner_radius=20,
        )

        remainingTemp = CTkLabel(
            remainingFrame,
            text="",
            width=550,
            height=0,
            bg_color=transparent,
            fg_color=transparent,
        )
        remainingTemp.grid(row=0, column=1, columnspan=80)

        remainingLabel = CTkLabel(
            remainingFrame,
            text="Remaining :",
            text_color=white,
            font=(lucida, 22),
            fg_color=transparent,
            bg_color=transparent,
        )
        remainingLabel.grid(row=0, column=1)

        remainingValue = CTkLabel(
            remainingFrame,
            text="0" + " ",
            text_color=white,
            font=(lucida, 22),
            fg_color=transparent,
            bg_color=transparent,
        )
        remainingValue.grid(row=0, column=80)

        def calculateRemaining(paid):
            self.remaining = float(paid) - float(price)
            remainingValue.configure(text=self.remaining)

        paid = StringVar()

        paid.trace(
            "w", lambda name, index, mode, paid=paid: calculateRemaining(paid.get())
        )

        paidEntry = CTkEntry(
            paidFrame,
            width=550,
            height=35,
            textvariable=paid,
            corner_radius=10,
            border_width=0,
            fg_color=white,
            bg_color=transparent,
            text_color=black,
            font=(normal, 16),
            placeholder_text="Paid",
            placeholder_text_color=grey,
        )
        paidEntry.grid(row=2, column=0, columnspan=80)

        def calculateRemainingWithDiscount(discount):
            remainingValue.configure(
                text=self.remaining + float(discount) / 100 * float(price)
            )

        discountValue = StringVar(value=0)

        discountValue.trace(
            "w",
            lambda name, index, mode, discountValue=discountValue: calculateRemainingWithDiscount(
                discountValue.get()
            ),
        )

        discountEntry = CTkEntry(
            discountFrame,
            width=550,
            height=35,
            textvariable=discountValue,
            corner_radius=10,
            border_width=0,
            fg_color=white,
            bg_color=transparent,
            text_color=black,
            font=(normal, 16),
            placeholder_text="Discount",
            placeholder_text_color=grey,
        )
        discountEntry.grid(row=2, column=0, columnspan=80)

        remainingFrame.grid(row=4, column=1, pady=20, padx=30)

        buttonsFrame = CTkFrame(
            mainFrame,
            fg_color=transparent,
            bg_color=transparent,
            corner_radius=20,
        )

        buttonsTemp = CTkLabel(
            buttonsFrame,
            text="",
            width=550,
            height=0,
            bg_color=transparent,
            fg_color=transparent,
        )
        buttonsTemp.grid(row=0, column=1, columnspan=9)

        def toMenuScreen():
            self.root.destroy()
            from d_menu_screen import MenuScreen

            MenuScreen(selection)

        buttonBack = CTkButton(
            buttonsFrame,
            width=150,
            height=50,
            text="Back",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 22),
            corner_radius=16,
            command=toMenuScreen,
        )
        buttonBack.grid(row=0, column=1)

        def toRecieptScreen():
            self.root.destroy()
            if selection == "takeaway":
                from g_reciept_screen import RecieptScreen

                RecieptScreen(price, selection, client, orders)
            elif selection == "cafe":
                from h_success_screen import SuccessScreen

                SuccessScreen()

        buttonNext = CTkButton(
            buttonsFrame,
            width=150,
            height=50,
            text="Next",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 22),
            corner_radius=16,
            command=toRecieptScreen,
        )
        buttonNext.grid(row=0, column=9)

        buttonsFrame.grid(row=5, column=1, pady=(20, 40), padx=30)

        mainFrame.place(anchor="center", relx=0.5, rely=0.5)

        self.root.mainloop()
