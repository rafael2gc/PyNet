number_list = list(range(1, 10))
#print(number_list)
for number in number_list:
    if number > 3:
        print(f"{number}th")
    elif number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
