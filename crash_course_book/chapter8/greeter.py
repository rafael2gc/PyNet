def get_formated_name(first_name, last_name):
    """ gets first and last names and deliveries it neatly formated """
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("Please tell me your name")
    print("enter 'q' at any time to quit")
    f_name = input("First Name:")
    if f_name == 'q':
        break
    l_name = input("Last Name:")
    if l_name == 'q':
        break
    formated_name = get_formated_name(f_name, l_name)
    print(f"\n Hello {formated_name} !")
