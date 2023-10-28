from tkinter import *
import sys
from tkinter import messagebox

sys.path.insert(0, "values")
sys.path.insert(0, "database")
from colors import *
from fonts import *
from customtkinter import *
from db_controller import *
from PIL import Image


class ClientSearchScreen:
    def __init__(self, price, selection, orders):
        connection = openConnection()
        self.root = Tk()
        self.root.title("Client Search")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        titleLabel = Label(
            self.root,
            font=(lucida, 40),
            text="Client Search",
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
            corner_radius=20,
        )

        toolsFrame = CTkFrame(
            mainFrame,
            fg_color=transparent,
            bg_color=transparent,
            width=700,
            height=200,
        )

        searchFrame = CTkFrame(
            toolsFrame,
            fg_color=transparent,
            bg_color=transparent,
            width=700,
            height=70,
        )

        searchLabel = CTkLabel(
            searchFrame,
            text="Phone Number",
            font=(lucida, 24),
        )
        searchLabel.grid(row=0, column=0, padx=(50, 0), pady=(0, 10))

        searchEntry = CTkEntry(
            searchFrame,
            width=700,
            height=35,
            corner_radius=10,
            border_width=0,
            fg_color=white,
            text_color=black,
            font=(normal, 16),
            placeholder_text="Phone Number",
            placeholder_text_color=grey,
        )
        searchEntry.grid(row=1, column=0, columnspan=80, padx=50)

        searchFrame.grid(row=0, column=0, rowspan=1, columnspan=8, pady=(40, 0))

        def toClientAddScreen():
            self.root.destroy()
            from e2_client_add_screen import ClientAddScreen

            ClientAddScreen(price, selection, orders)

        buttonAdd = CTkButton(
            toolsFrame,
            width=250,
            height=50,
            text="Add Client",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 22),
            corner_radius=16,
            command=toClientAddScreen,
        )
        buttonAdd.grid(row=2, column=2, pady=40)

        toolsFrame.grid(row=0, column=0, padx=20)

        detailsframe = CTkFrame(
            mainFrame,
            fg_color=darkBlue,
            bg_color=transparent,
            corner_radius=20,
        )

        idLabel = CTkLabel(
            detailsframe,
            text="Id",
            font=(lucida, 20),
            width=40,
        )
        idLabel.grid(row=0, column=1, pady=(20, 0))

        nameLabel = CTkLabel(
            detailsframe,
            text="Name",
            font=(lucida, 20),
            width=240,
        )
        nameLabel.grid(row=0, column=2, pady=(20, 0))

        addressLabel = CTkLabel(
            detailsframe,
            text="Address",
            font=(lucida, 20),
            width=340,
        )
        addressLabel.grid(row=0, column=3, pady=(20, 0))

        buttonTempLabel = CTkLabel(
            detailsframe,
            text="",
            font=(lucida, 20),
            fg_color=transparent,
            bg_color=transparent,
            width=80,
        )
        buttonTempLabel.grid(row=0, column=4, pady=(20, 0))

        showIdLabel = CTkLabel(
            detailsframe,
            text="1",
            font=(normal, 20),
            text_color=white,
        )

        showNameLabel = CTkLabel(
            detailsframe,
            text="Ahmed Essam Eliwa",
            font=(normal, 20),
            text_color=white,
        )

        showAddressLabel = CTkLabel(
            detailsframe,
            text="EQalyoubia - Shoubra - Basos - B7b7",
            font=(normal, 20),
            text_color=white,
        )

        def selectClient():
            self.root.destroy()
            from f_cash_screen import CashScreen

            CashScreen(price, selection, self.client, orders)

        buttonSelect = CTkButton(
            detailsframe,
            width=60,
            height=30,
            text="Select",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 20),
            corner_radius=10,
            command=selectClient,
        )

        detailsframe.grid(row=1, column=0, padx=(20, 0), pady=(0, 40))

        def searchClientClick():
            phoneNumber = searchEntry.get()
            if not phoneNumber.isdigit():
                messagebox.showerror("Error", "Phone number is not valid")
            else:
                try:
                    self.client = searchClient(connection, phoneNumber)
                    showIdLabel.configure(text=self.client.id)
                    showNameLabel.configure(text=self.client.name)
                    showAddressLabel.configure(text=self.client.address)

                    showIdLabel.grid(row=1, column=1)
                    showNameLabel.grid(row=1, column=2)
                    showAddressLabel.grid(row=1, column=3)
                    buttonSelect.grid(row=1, column=4, padx=20)
                except:
                    messagebox.showerror("Error", "Client not found, Try adding new")

        buttonSearch = CTkButton(
            toolsFrame,
            width=250,
            height=50,
            text="Search",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 22),
            corner_radius=16,
            command=searchClientClick,
        )
        buttonSearch.grid(row=2, column=5, pady=40)

        mainFrame.place(anchor="center", relx=0.5, rely=0.5)

        self.root.mainloop()
        endConnection(connection)
