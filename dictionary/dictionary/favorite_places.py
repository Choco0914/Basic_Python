favorite_places = {'han' : ['home', "'he's room"],
    'rick' : ['cafe', 'school'],
    'cristiano' : ['soccer ground', 'workout space']}
for person, spaces in favorite_places.items():
    print(person.title() + ' likes ' + str(spaces[0]).title() + ', ' +
     str(spaces[1]).title() )
