age = input("Enter Age: ")
print(type(age))
age = int(age)
print(type(age))
if age <= 2:
    print("The person is a baby")
elif age > 2 and age < 4:
    print("The person is a Toddler")
elif age >= 4 and age < 13:
    print("The person is a kid")
elif age >= 13 and age < 20:
    print("The person is a teenager")
elif age >= 20 and age < 65:
    print("The person is a adult")
else:
    print("The person is a elder")
