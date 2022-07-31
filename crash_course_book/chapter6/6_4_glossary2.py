glossary = {
        'string': 'Any sequence of caracters',
        'boolean': 'binary data type, yes/no, true/false',
        'list': 'It is a list of values',
        'integer': 'whole numbers',
        'dictionaries': 'key value list'
        }
for key, value in glossary.items():
    print(f" A {key} is  {value}")
glossary['color'] = 'green'
glossary['points'] = 5

print('-' * 30)

for key, value in glossary.items():
    print(f"\n A {key} is  {value}")

