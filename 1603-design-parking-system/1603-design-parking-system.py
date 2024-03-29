class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parkingSpace = ['_',big,medium,small]

    def addCar(self, carType: int) -> bool:
        if self.isParkingAvailable(carType):
            self.parkingSpace[carType] -= 1
            return True
        return False
    
    def isParkingAvailable(self, carType):
        return self.parkingSpace[carType] > 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)