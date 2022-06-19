# Step1 - Changing, Adding and removing elements from a list
sa_countries = ['uruguay', 'argentina', 'paraguay', 'chile', 'brazil', 'peru', 'colombia', 'equador', 'bolivia', 'venezuela']
print("\nAdding, Changing and Removing elements from the list:\n")
print(f"{sa_countries}\n")
print('-' * 30)

sa_countries.append('Suriname')
print(f"Added Suriname our list\n")
print(f"{sa_countries}\n")

sa_countries.insert(3,'French Guiana')
print('-' * 30)
print(f"\nINSERTED French Guiana into the 4th position of the list\n")
print(f"{sa_countries}\n")

del sa_countries[-1]
print('-' * 30)
print(f"\nDELETING the last element of the list\n")
print(f"{sa_countries}\n")

popped = sa_countries.pop()
print('-' * 30)
print(f"\nPOPPING the last element of the list\n")
print(f"{sa_countries}\n")
print(f"{popped} Was POPed from the list")


popped = sa_countries.pop(1)
print('-' * 30)
print(f"\nPOPPING the seccond element of the list\n")
print(f"{sa_countries}\n")
print(f"{popped} Was POPed from the list")


out = 'peru'
sa_countries.remove(out)
print('-' * 30)
print(f"\nRemoving from the list by Value\n")
print(f"{out}\n")
print(f"{sa_countries}\n")
