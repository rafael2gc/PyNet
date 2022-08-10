prompt = "Add toppings to your pizza:"
prompt +="Entrer the topping name:"
lista = []
print(type(lista))
flag = True
while flag:
    topping = input(prompt)
    if topping != 'quit':
        #print(f"{topping} added to your piza!!")
        lista.append(topping)
    else:
        for i in lista:
            print(f"\n\t- {i}")
       # print(lista)
        flag = False
