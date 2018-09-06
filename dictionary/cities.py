cities = {'seoul' : {'country' : 'korea',
        'population' : '986 milion',
        'fact' : 'good place'},
    'new york' : {'country' : 'usa',
        'population' : '850 milion',
        'fact' : 'spidermen home'},
    'london' : {'country' : 'uk',
        'population' : '870 milion',
        'fact' : 'doctor who lived in uk'}
    }
for citi, citi_info in cities.items():
        print(citi.title() + ":")
        citico = citi_info['country']
        citipo = citi_info['population']
        citifa = citi_info['fact']
        print('\tCountry: ' + citico.upper() )
        print('\tPopulation: ' + citipo)
        print('\tFact: ' + citifa)
