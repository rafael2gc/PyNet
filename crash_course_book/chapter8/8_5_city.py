def describe_city(city, country = 'Brasil'):
    """ simple message about city and country """
    print(f"{city.title()} is in {country.title()}")
describe_city('Rio de Janeiro')
print('\n***********************')

describe_city('Vitoria')
print('\n***********************')

describe_city('Londres', 'england')
