class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.b = big
        self.m = medium
        self.s = small 
    def addCar(self, carType):
        if carType == 1 and self.b > 0:
            self.b = self.b - 1
            return True
        elif carType == 2 and self.m > 0:
            self.m = self.m -1
            return True
        elif carType == 3 and self.s > 0:
            self.s = self.s -1
            return True
        else:
            return False
