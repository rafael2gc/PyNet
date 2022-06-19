list = ['bob', 'cassia', 'mozart']
print(f'Dear {list[0]} i would like to invite you for a dinner')
print(f'Dear {list[1]} i would like to invite you for a dinner')
print(f'Dear {list[2]} i would like to invite you for a dinner')
new_person = list.pop()
print(f'\nSorry Rafael,  but {new_person} cant  make it to the dinner\n')
list.insert(2, 'chico')
print(f'Dear {list[0]} i would like to invite you for a dinner')
print(f'Dear {list[1]} i would like to invite you for a dinner')
print(f'Dear {list[2]} i would like to invite you for a dinner')


