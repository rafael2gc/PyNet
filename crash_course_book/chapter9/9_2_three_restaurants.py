class Restaurant:
    """ simple class to define a restaurant """
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restautant")

    def open_restaurant(self):
        print(f"{self.name} is OPEN !!")

my_rest1 = Restaurant('flor do para', 'comida do norte')
my_rest2 = Restaurant('Garota de Ipanema', 'comida de boteco')
my_rest3 = Restaurant('Zaitoon', 'Persian food')

my_rest1.describe_restaurant()
my_rest2.describe_restaurant()
my_rest3.describe_restaurant()
