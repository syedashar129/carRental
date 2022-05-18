# Reserve a car
# Search for a car
# cancel a reservation
# modify a reservation
# sign up
# log in



##import another class

file = open('car.txt', 'w')
file.write('Toyota')
file.close()


class Vehicle:
    make = ''
    model = ''
    year = 0
    mileage = 0
    isRented = False

    def __init__(self, make, model, year, mileage, isRented):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.isRented = isRented

    #getMethods for vehicle
    def getVehicle(self):
        pass


    #set methods for vehicle
    def setMake(self):
        pass

    def setModel(self):
        pass

    def setYear(self):
        pass

    def setMileage(self):
        pass

    def setisRented(self):
        pass

if __name__ == '__main__':
    v = Vehicle('Toyota', 'Camry', 2022, 5000, False)
    print(v.isRented)


