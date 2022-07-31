rivers = {
        'nile': 'egipt',
        'amazon': 'brasil',
        'yellow': 'china',
        }
for key, value in rivers.items():
    print(f"River {key} runs in  {value}")
print('-' * 30)
for key in rivers.keys():
    print(key)

print('-' * 30)
for value in rivers.values():
    print(value)
