favorite_number = {
        'rafael': [9, 171, 44],
        'Otto': [14, 4, 2014],
        'julia': [14, 69, 60, 1984],
        'laura': [2, 11, 2011],
        }
for key, numbers in favorite_number.items():
    print(f"{key.title()}'s favorite numebers are:")
    for number in numbers:
        print(f"- {number}")
