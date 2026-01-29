class computer:
    def __init__(self):
        self.__maxPrice = 700
    def sell(self):
        print("Selling Price: {}".format(self.__maxPrice))

    def setMaxPrice(self, price):
        self.__maxPrice = price

c = computer()
c.sell()
c.__maxPrice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()