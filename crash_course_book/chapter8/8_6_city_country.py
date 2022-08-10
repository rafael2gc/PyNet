def city_country(city, country):
    """ gets a city and country and format it neatly """
    return(city.title() + ',' + country.title())
city = city_country('vitoria', 'brasil')
print(city)

city = city_country('roma', 'italia')
print(city)
