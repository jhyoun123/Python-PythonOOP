class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price: ", self.price
        print "Maximum speed: " + self.max_speed
        print "Total Miles: ", self.miles
    def ride(self):
        print "Riding..."
        self.miles += 10
    def reverse(self):
        print "Reversing..."
        self.miles -= 5

bike1 = Bike(200, "25mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(100, "50mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(400, "35mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()