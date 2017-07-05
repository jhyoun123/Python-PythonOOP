class Product(object):
    def __init__(self, price, name, weight, brand, cost, status):
        self.price = price 
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax):
        return self.cost * (1 + tax)
    def Return(self, reason):
        if (reason == "defective"):
            self.status = "defective"
            self.cost = 0
        elif (reason == "box"):
            self.status = "for sale"
        elif (reason == "opened"):
            self.status = "used"
            self.cost = cost * .8
        return self
    def displayInfo(self):
        print 'Price: ' + str(self.price)
        print 'Name: ' + str(self.name)
        print 'Weight: ' + self.weight
        print 'Brand: ' + str(self.brand)
        print 'Cost: ' + str(self.cost)
        print 'Status: ' + str(self.status)
        return self