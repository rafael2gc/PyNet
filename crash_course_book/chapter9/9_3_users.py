class User:
    """ simple class describing an user """
    def __init__(self, first_name, last_name, dob, email):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email

    def describe_user(self):
        print(f"\nName = {self.first_name} {self.last_name}\nDOB = {self.dob}\nEmail = {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

user1 = User('Rafael', 'Giuri Costa', '09/07/1978', 'rafael2gc@gmail.com')

user1.describe_user()
user1.greet_user()
