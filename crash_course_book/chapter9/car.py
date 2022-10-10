""" A class that can be used to represent a Car """

class Car:
    """ a simple attempt to represent a car """
    def __init__(self, make, model, year):
        """ initiate the attributes for class car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descritive_name(self):
        """ return a neatly formated descritive name """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ print an statement showing the car mileage """
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        set the odometer reading to the givem value.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading """
        self.odometer_reading += miles
