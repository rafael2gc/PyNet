sandwich_orders = ['pao com salame', 'hamburger', 'cheeseburger', 'misto quente', 'x-banana']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)
print(f"\nList of sandwiches made so far:")
for sambo in finished_sandwiches:
    print(f"\t- {sambo}")
