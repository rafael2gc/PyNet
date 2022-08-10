sandwich_orders = ['pao com salame', 'pastrami', 'hamburger', 'pastrami', 'cheeseburger', 'misto quente', 'pastrami', 'x-banana']
finished_sandwiches = []
print(f"\nSorry, we run out of Pastrami Sandwich")
print(f"**************************************")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)
print(f"\nList of sandwiches made so far:")
for sambo in finished_sandwiches:
    print(f"\t- {sambo}")
