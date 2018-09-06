lee = {'first name' : '순신',
    'last name' : '이',
    'age' : 53,
    'city' : '조선 한성부 건천동',}
ho = {'first name' : 'ronaldo',
    'last name' : 'cristiano',
    'age' : 33,
    'city' : 'Torino'}
bail ={'first name' : 'bale',
    'last name' : 'gareth',
    'age' : 29,
    'city' : 'mardrid'}
people = [lee, ho, bail]

for person in people:
        full_name = person['last name'] + " " + person['first name']
        age = person['age']
        city = person['city']

        print("\nName is " + full_name.title())
        print("\tage: " +  str(age))
        print("\tcity: " + city.title())
