person_1 = {'first_name': 'Rafael', 'last_name': 'Costa', 'age': '44', 'city': 'Dublin'}
person_2 = {'first_name': 'Otto', 'last_name': 'Giuri', 'age': '8', 'city': 'vix'}
person_3 = {'first_name': 'Laura', 'last_name': 'Fonseca Giuri Costa', 'age': '10', 'city': 'rio'}
people = [person_1, person_2, person_3]

for person in people:
    print(f"{person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['city']}")
