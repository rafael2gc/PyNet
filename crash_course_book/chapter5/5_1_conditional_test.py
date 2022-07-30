car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

toppings_list = ['alho', 'parmesan', 'bacon', 'salad']
topping = 'alho'
if topping in toppings_list:
    print(f"Yes, we have {topping}")
print(topping in toppings_list)
age1 = 23
age2 = 75
print(age1 > 12 or age2 < 10)
banned_users = ['hudson', 'alisson',  'diego']
print('mateus' in banned_users)
print('hudson' in banned_users)
user = 'otto'
if user not in  banned_users:
    print('user' in banned_users)
    print(f"{user.upper()} make a post")
n1 = 10
n2 = 20
print(n1 + n2 > 31)
print(n1 + n2 < 31)

print( '#' * 10)
print(n1 > 11 and n2 > 11)

