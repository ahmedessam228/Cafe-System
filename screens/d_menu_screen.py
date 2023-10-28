import sys


sys.path.insert(0, "values")
sys.path.insert(0, "classes")
sys.path.insert(0, "database")
from colors import *
from fonts import *
from client import *
from bill import *
from order import *
from tkinter import *
from customtkinter import *
from db_controller import *


class MenuScreen:
    def __init__(self, selection):
        connection = openConnection()

        self.products = []
        self.buttons = list()
        self.selectedProduct = Product(id=0, name="None", category="None", price="None")
        self.totalPrice = 0.0
        self.thisQuantity = 0
        self.ordersBookmark = dict()
        self.orders = list()

        if selection == "takeaway":
            self.bill = Bill(getBillID(connection))

        self.root = Tk()
        self.root.title("Menu")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        categoryFrame = CTkFrame(
            self.root,
            fg_color=darkBlue,
            bg_color=transparent,
            corner_radius=0
        )
        categoryFrame.place(x=0, y=0)

        def hotDrinksCategoryValue():
            destroy(self.buttons)
            self.products = getMenu(connection, "Hot Drinks")
            showProducts(self.products)


        hotDrinksCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Hot Drinks",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=hotDrinksCategoryValue
        )
        hotDrinksCategoryButton.grid(row=1, column=0, pady=((height - 170) / 20), padx=15)

        def coffeeCategoryValue():
            destroy(self.buttons)
            self.products = getMenu(connection, "Coffee")
            showProducts(self.products)

        coffeeCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Coffee",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=coffeeCategoryValue
        )
        coffeeCategoryButton.grid(row=2, column=0, pady=((height - 170) / 20), padx=15)

        def iceCreamCategoryValue():
            destroy(self.buttons)
            self.products = getMenu(connection, "Ice Cream")
            showProducts(self.products)

        IceCreamCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Ice Creams",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=iceCreamCategoryValue
        )
        IceCreamCategoryButton.grid(row=3, column=0, pady=((height - 170) / 20), padx=15)

        def dessertCategoryValue():
            destroy(self.buttons)
            self.products = getMenu(connection, "Dessert")
            showProducts(self.products)

        dessertCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Desserts",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=dessertCategoryValue
        )
        dessertCategoryButton.grid(row=4, column=0, pady=((height - 170) / 20), padx=15)

        def softDrinksCategoryValue():
            destroy(self.buttons)
            self.products = getMenu(connection, "Soft Drinks")
            showProducts(self.products)

        softDrinksCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Soft Drinks",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=softDrinksCategoryValue
        )
        softDrinksCategoryButton.grid(row=5, column=0, pady=((height - 170) / 20), padx=15)

        productFrame = CTkScrollableFrame(
            self.root,
            fg_color=transparent,
            bg_color=transparent,
            width=width - 220,
            height=height - 100,
            corner_radius=0,
            scrollbar_button_color= darkBlue,
            scrollbar_button_hover_color= cafe,
        )
        productFrame.place(x=200, y=0)

        selectedProductDetailsFrame = CTkFrame(
            self.root,
            fg_color=darkBlue,
            bg_color=transparent,
            corner_radius=0,
        )
        selectedProductDetailsFrame.pack(side="bottom")

        productNameLabel = CTkLabel(
            selectedProductDetailsFrame,
            text="Name : ",
            font=(lucida, 20),
            text_color=white,
            height=100,
            width=100,
            bg_color=transparent,
            fg_color=transparent,
        )
        productNameLabel.grid(row=1, column=1, padx=((width - 880) / 20))

        productNameValue = CTkLabel(
            selectedProductDetailsFrame,
            text="None",
            font=(lucida, 20),
            bg_color=transparent,
            fg_color=transparent,
            text_color=white,
            width=200,
            wraplength=200,
        )
        productNameValue.grid(row=1, column=2, pady=20, padx=((width - 880) / 20))

        productQuantityLabel = CTkLabel(
            selectedProductDetailsFrame,
            text="Quantity : ",
            font=(lucida, 20),
            width=120,
            bg_color=transparent,
            fg_color=transparent,
        )
        productQuantityLabel.grid(row=1, column=3, pady=20, padx=((width - 880) / 20))

        def removeItem():
            if self.thisQuantity > 0:
                self.thisQuantity -= 1
                productQuantityValue.configure(text=self.thisQuantity)
                self.totalPrice -= self.selectedProduct.price
                productPricevalue.configure(text=self.totalPrice)
                productIndex = self.ordersBookmark[self.selectedProduct.name]
                self.orders[productIndex].count -= 1
                self.orders[productIndex].totalPrice -=  float(self.selectedProduct.price)

        productQuantityMinusButton = CTkButton(
            selectedProductDetailsFrame,
            width=60,
            height=60,
            text="-",
            text_color=darkBlue,
            hover_color=cafe,
            fg_color=white,
            bg_color=darkBlue,
            font=(normal, 30, "bold"),
            corner_radius=20,
            command=removeItem
        )
        productQuantityMinusButton.grid(row=1, column=5, padx=((width - 880) / 20))

        productQuantityValue = CTkLabel(
            selectedProductDetailsFrame,
            text="0",
            font=(lucida, 20),
            width=60,
            bg_color=transparent,
            fg_color=transparent,
        )
        productQuantityValue.grid(row=1, column=6, pady=20, padx=((width - 880) / 20))

        def addItem():
            self.thisQuantity += 1
            productQuantityValue.configure(text=self.thisQuantity)
            self.totalPrice += self.selectedProduct.price
            productPricevalue.configure(text=self.totalPrice)
            productIndex = self.ordersBookmark[self.selectedProduct.name]
            self.orders[productIndex].count += 1
            self.orders[productIndex].totalPrice +=  float(self.selectedProduct.price)

        productQuantityPlusButton = CTkButton(
            selectedProductDetailsFrame,
            width=60,
            height=60,
            text="+",
            text_color=darkBlue,
            hover_color=cafe,
            fg_color=white,
            bg_color=darkBlue,
            font=(normal, 30, "bold"),
            corner_radius=20,
            command=addItem
        )
        productQuantityPlusButton.grid(row=1, column=7, padx=((width - 880) / 20))

        productPriceLabel = CTkLabel(
            selectedProductDetailsFrame,
            text="Total Price :  ",
            font=(lucida, 20),
            width=150,
            bg_color=transparent,
            fg_color=transparent,
        )
        productPriceLabel.grid(row=1, column=8, pady=20, padx=((width - 880) / 20))

        productPricevalue = CTkLabel(
            selectedProductDetailsFrame,
            text="0.0",
            font=(lucida, 20),
            bg_color=transparent,
            fg_color=transparent,
            width=100,
            wraplength=100
        )
        productPricevalue.grid(row=1, column=9, pady=20, padx=((width - 880) / 20))

        def toNextScreen():
            price = self.totalPrice
            self.root.destroy()
            if selection == "takeaway":
                from e1_client_search_screen import ClientSearchScreen
                ClientSearchScreen(price, selection, self.orders)
            elif selection == "cafe":
                from f_cash_screen import CashScreen
                CashScreen(price, selection, Client("None", "None", "None"), self.orders)

        proceedButton = CTkButton(
            selectedProductDetailsFrame,
            width=100,
            height=50,
            text="→",
            text_color=darkBlue,
            hover_color=cafe,
            fg_color=white,
            bg_color=darkBlue,
            font=(normal, 30, "bold"),
            corner_radius=20,
            command=toNextScreen,
        )
        proceedButton.grid(row=1, column=10, padx=((width - 880) / 20))


        def destroy(buttons):
            for i in range(0, len(buttons)):
                buttons[i].destroy()

        def getDetails(i):
            self.selectedProduct = self.products[i]
            product = self.selectedProduct
            productNameValue.configure(text=product.name)
            if not product.name in self.ordersBookmark:
                self.thisQuantity = 1
                self.ordersBookmark[product.name] = len(self.orders)
                if selection == "takeaway":
                    self.orders.append(Order(self.bill.id, product.name, self.thisQuantity, int(self.thisQuantity) * product.price))
                elif selection == "cafe":
                    self.orders.append(Order(0, product.name, self.thisQuantity, int(self.thisQuantity) * product.price))
                productQuantityValue.configure(text=self.thisQuantity)
            else:
                productIndex = self.ordersBookmark[product.name]
                self.orders[productIndex].count += 1
                self.thisQuantity = self.orders[productIndex].count
                self.orders[productIndex].totalPrice +=  float(self.selectedProduct.price)
                productQuantityValue.configure(text=self.orders[productIndex].count)
            self.totalPrice += product.price
            productPricevalue.configure(text=self.totalPrice)

        def showProducts(products):
            c = 1
            r = 1
            for i in range(0, len(products)):
                if c == 5:
                    c = 1
                    r += 1
                product = products[i]
                productItem = CTkButton(
                    productFrame,
                    width=240,
                    height=150,
                    text=str(product.name) + "\n" + str(product.price),
                    hover=True,
                    hover_color=darkBlue,
                    text_color=white,
                    fg_color=cafe,
                    bg_color=transparent,
                    font=(normal, 25),
                    corner_radius=25,
                    command=lambda i=i: getDetails(i)
                )
                self.buttons.append(productItem)
                productItem._text_label.configure(wraplength=200)
                productItem.grid(row=r, column=c, padx = ((width - 200) / 32), pady = 50)
                c+=1

        self.root.mainloop()
        endConnection(connection)
