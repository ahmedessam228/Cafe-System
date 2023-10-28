class Bill:#, customerId, orderId, totalPrice, date, time
    def __init__(self, id):
        self.id = id
        # self.customerId = customerId
        # self.orderId = orderId
        # self.totalPrice = totalPrice
        # self.date = date
        # self.time = time
    
    def addBillDetails(self, customerId, orderId, totalPrice):
        self.customerId = customerId
        self.orderId = orderId
        self.totalPrice = totalPrice
