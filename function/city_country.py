def city_country(city, country):
    full_information = city + ', ' + country
    return full_information.title()

cities = city_country('santiago', 'chile')
print(cities)

cities1 = city_country('seoul', 'korea')
print(cities1)

cities2 = city_country('berllin', 'germany')
print(cities2)
