from tkinter import *
import sys

sys.path.insert(0, "values")
sys.path.insert(0, "classes")
sys.path.insert(0, "database")
from colors import *
from fonts import *
from customtkinter import *
from PIL import Image
from bill import *
from order import *
from db_controller import *


class RecieptScreen:
    def __init__(self, price, selection, client, orders):

        connection = openConnection()

        self.root = Tk()
        self.root.title("Reciept")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        titleFrame = Frame(self.root, bg=beige)
        titleFrame.grid()

        titleLabel = Label(
            titleFrame,
            font=(lucida, 40),
            text="Reciept",
            bg=beige,
        )
        titleLabel.grid(padx=10, pady=20)

        cup = Image.open("icons\cup.png")
        cup = cup.resize((80, 80))
        icon = CTkImage(light_image=cup, size=(80, 80))
        logo = CTkLabel(self.root, image=icon, bg_color=transparent, text="")
        logo.place(x=screenWidth - 100, y=15)

        mainFrame = CTkFrame(
            self.root,
            fg_color=darkBlue,
            bg_color=transparent,
            corner_radius=20,
        )

        detailsFrame = CTkFrame(
            mainFrame,
            fg_color=transparent,
            bg_color=transparent,
            corner_radius=20,
        )

        nameTemp = CTkLabel(
            detailsFrame,
            text="",
            width=500,
            height=0,
            bg_color=transparent,
            fg_color=transparent,
        )
        nameTemp.grid(row=0, column=0, columnspan=80)

        nameLabel = CTkLabel(
            detailsFrame,
            text="Name : ",
            font=(lucida, 20),
            text_color=white,
        )
        nameLabel.grid(row=0, column=0, pady=10)

        nameValue = CTkLabel(
            detailsFrame,
            text=client.name,
            font=(normal, 20),
            text_color=white,
        )
        nameValue.grid(row=0, column=80, pady=10)

        addressTemp = CTkLabel(
            detailsFrame,
            text="",
            width=500,
            height=0,
            bg_color=transparent,
            fg_color=transparent,
        )
        addressTemp.grid(row=1, column=0, columnspan=80)

        addressLabel = CTkLabel(
            detailsFrame,
            text="Address : ",
            font=(lucida, 20),
            text_color=white,
        )
        addressLabel.grid(row=1, column=0, pady=10)

        addressValue = CTkLabel(
            detailsFrame,
            text=client.address,
            font=(normal, 20),
            text_color=white,
        )
        addressValue.grid(row=1, column=80, pady=10)

        phoneTemp = CTkLabel(
            detailsFrame,
            text="",
            width=500,
            height=0,
            bg_color=transparent,
            fg_color=transparent,
        )
        phoneTemp.grid(row=2, column=0, columnspan=80)

        phoneLabel = CTkLabel(
            detailsFrame,
            text="Phone Number : ",
            font=(lucida, 20),
            text_color=white,
        )
        phoneLabel.grid(row=2, column=0, pady=10)

        phoneValue = CTkLabel(
            detailsFrame,
            text=client.phone,
            font=(normal, 20),
            text_color=white,
        )
        phoneValue.grid(row=2, column=80, pady=10)

        priceTemp = CTkLabel(
            detailsFrame,
            text="",
            width=500,
            height=0,
            bg_color=transparent,
            fg_color=transparent,
        )
        priceTemp.grid(row=3, column=0, columnspan=80)

        priceLabel = CTkLabel(
            detailsFrame,
            text="Price : ",
            font=(lucida, 20),
            text_color=white,
        )
        priceLabel.grid(row=3, column=0, pady=10)

        priceValue = CTkLabel(
            detailsFrame,
            text=str(price),
            font=(normal, 20),
            text_color=white,
        )
        priceValue.grid(row=3, column=80, pady=10)

        detailsFrame.grid(row=0, column=0, padx=30, pady=(20, 0))

        productFrame = CTkFrame(
            mainFrame,
            fg_color=transparent,
            bg_color=transparent,
            corner_radius=20,
        )

        productTemp = CTkLabel(
            productFrame,
            text="",
            width=700,
            height=0,
            bg_color=transparent,
            fg_color=transparent,
        )
        productTemp.grid(row=0, column=1, columnspan=9, pady=(0, 50))

        productNameLabel = CTkLabel(
            productFrame,
            text="Name",
            font=(lucida, 30, "bold"),
            text_color=white,
        )
        productNameLabel.grid(row=0, column=1)

        productCountLabel = CTkLabel(
            productFrame,
            text="Count",
            font=(lucida, 30, "bold"),
            text_color=white,
        )
        productCountLabel.grid(row=0, column=5)

        productPriceLabel = CTkLabel(
            productFrame,
            text="Price",
            font=(lucida, 30, "bold"),
            text_color=white,
        )
        productPriceLabel.grid(row=0, column=9)

        for i in range(0, len(orders)):
            productNameValue = CTkLabel(
                productFrame,
                text=orders[i].name,
                font=(lucida, 20),
                text_color=white,
            )
            productNameValue.grid(row=i + 1, column=1)

            productCountValue = CTkLabel(
                productFrame,
                text=orders[i].count,
                font=(lucida, 20),
                text_color=white,
            )
            productCountValue.grid(row=i + 1, column=5)

            productPriceValue = CTkLabel(
                productFrame,
                text=orders[i].totalPrice,
                font=(lucida, 20),
                text_color=white,
            )
            productPriceValue.grid(row=i + 1, column=9)

        productFrame.grid(row=1, column=0, padx=30, pady=(30, 50))

        buttonsFrame = CTkFrame(
            mainFrame,
            fg_color=transparent,
            bg_color=transparent,
            corner_radius=20,
        )

        buttonsTemp = CTkLabel(
            buttonsFrame,
            text="",
            width=500,
            height=0,
            bg_color=transparent,
            fg_color=transparent,
        )
        buttonsTemp.grid(row=0, column=1, columnspan=9)

        def toCashScreen():
            self.root.destroy()
            from f_cash_screen import CashScreen

            CashScreen(price, selection, client)

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
            command=toCashScreen,
        )
        buttonBack.grid(row=0, column=1)

        def toSuccessScreen():
            addOrdertoDB(connection, orders)

            bill = Bill(orders[0].id)
            bill.addBillDetails(client.id, orders[0].id, price)
            addBilltoDB(connection, bill)

            self.root.destroy()
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
            command=toSuccessScreen,
        )
        buttonNext.grid(row=0, column=9)

        buttonsFrame.grid(row=2, column=0, pady=(20, 40), padx=30)

        mainFrame.place(anchor="center", relx=0.5, rely=0.5)

        self.root.mainloop()
        endConnection(connection)
