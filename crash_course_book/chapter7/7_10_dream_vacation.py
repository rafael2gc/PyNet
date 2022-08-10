prompt = "If you could visity one place one earth, where would you go?"
prompt += "\nType quit to finish\n"
lista = []
active = True
while active:
    place = input(prompt)
    if place != 'quit':
        lista.append(place)
    else:
        for i in lista:
            print(f"\n{i}")
            active = False
