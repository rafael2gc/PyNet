list = ['bob', 'cassia', 'mozart']
list.insert(0, 'chico')
list.insert(4, 'cartola')
list.insert(2, 'curt')


print("\nBad news guys, i can only take 2 for dinner, sorry about that.\n")

uninvite = list.pop()
print(f"\nSorry {uninvite}, i can't take you to dinner")
uninvite = list.pop()
print(f"\nSorry {uninvite}, i can't take you to dinner")
uninvite = list.pop()
print(f"\nSorry {uninvite}, i can't take you to dinner")
uninvite = list.pop()
print(f"\nSorry {uninvite}, i can't take you to dinner\n")

print(f"Hello {list[0]} you're invited for our grand dinner")
print(f"Hello {list[1]} you're invited for our grand dinner")
del list[0]
del list[0]
print(len(list))
