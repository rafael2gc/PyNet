cities = {
        'ny': {'country': 'USA', 'population': '12 Milion', 'fact': 'super cold'},
        'sao paulo': {'country': 'brasil', 'population': '18 Milion', 'fact': 'Dangerous'},
        'london' : {'country': 'england', 'population': '8 Milion', 'fact': 'they have a real family'},
        'tokio': {'country': 'japan', 'population': '24 Milion', 'fact': 'crazy japs'},
        }
for city, data in cities.items():
    print(f"\nInformacoes sobre {city.title()}:")
    for key, value in data.items():
        print(f"- {key.title()}: {value.title()}")
