import sqlite3
import sys
sys.path.insert(0, "classes")
from product import Product
from client import Client
from order import Order


def openConnection():
    connection = sqlite3.connect("database\cafe.db")
    print("connection opened")
    return connection


def endConnection(connection):
    connection.close()
    print("connection ended")


def addClient(connection, client):
    cursor = connection.cursor()
    cursor.execute(
        """
        insert into Customer(Name, Phone, Address) values (?, ?, ?)
        """,
        (client.name, client.phone, client.address),
    )
    connection.commit()


def getMenu(connection, category):
    cursor = connection.cursor()
    result = cursor.execute("select * from Product where category = ?", ([category])).fetchall()
    products = list()
    for product in result:
        if product[0] != 0:
            products.append(Product(id=product[0], name=product[1], category=product[2], price=product[3]))
    connection.commit()
    return products

def searchClient(connection, number):
    cursor = connection.cursor()
    result = cursor.execute("select * from Customer where Phone = ?", ([number])).fetchone()
    client = Client(name=result[1], phone=result[2], address=result[3])
    client.addId(result[0])
    return client

def getBillID(connection):
    cursor = connection.cursor()
    result = cursor.execute("select * from Bill").fetchall()
    if (len(result) - 1) < 0:
        return 1
    else:
        return result[len(result) - 1][0] + 1

def addBilltoDB(connection, bill):
    cursor = connection.cursor()
    cursor.execute(
        """
        insert into Bill(Cust_ID, Order_ID, Total_Price) values (?, ?, ?)
        """,
        (bill.customerId, bill.orderId, bill.totalPrice),
    )
    connection.commit()

def addOrdertoDB(connection, orders):
    cursor = connection.cursor()
    for order in orders:
        cursor.execute(
            """
            INSERT INTO Order_Items(Bill_ID, Product_Count, Total_Price, Product_Name) values (?, ?, ?, ?)
            """,
            (order.id, order.count, order.totalPrice, str(order.name)),
        )
    connection.commit()
