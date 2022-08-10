prompt = "Enter your age:"
flag = True
while flag:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("FREE Ticket")
    elif age >= 3 and age <= 12:
        print("Ticket Cost is 10 Euros")
    elif age >= 12:
        print("Ticket Cost is 15 Euros")
