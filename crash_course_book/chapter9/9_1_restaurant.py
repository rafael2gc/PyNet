class Restaurant:
    """ simple class to define a restaurant """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restautant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is OPEN !!")

my_rest = Restaurant('flor do para', 'comida do norte')

my_rest.describe_restaurant()
my_rest.open_restaurant()
