class User:
    """ simple class describing an user """
    def __init__(self, first_name, last_name, dob, email):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nName = {self.first_name} {self.last_name}\nDOB = {self.dob}\nEmail = {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Rafael', 'Giuri Costa', '09/07/1978', 'rafael2gc@gmail.com')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

class Admin(User):
    def __init__(self, first_name, last_name, dob, email):
        super().__init__(first_name, last_name, dob, email)
        self.privileges = []

    def show_privileges(self):
        print(f"User {self.first_name} has the rigths:")
        for privilege in self.privileges:
            print(f"- {privilege}")

user2 =  Admin('regilson', 'okpok', '01/01/1111', 'z@zp.com')
user2.privileges = ['can add', 'can delete', 'can edit']

user2.show_privileges()

