number = input("Type a number: ")
number = int(number)
if number % 10 == 0:
    print(f"{str(number)} is multple of 10")
else:
    print(f"{str(number)} is NOT a multiple of 10")
