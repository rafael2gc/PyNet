class Restaurant:
    """ simple class to define a restaurant """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restautant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is OPEN !!")

    def print_served(self):
        print(f"We have served {self.number_served} so far.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

my_rest = Restaurant('flor do para', 'comida do norte')

my_rest.set_number_served(8)
my_rest.increment_number_served(1)
my_rest.print_served()
