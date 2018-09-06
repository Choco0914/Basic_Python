golden_retriver = {'name' : 'golden retriver',
    'master' : 'matt',
    'type' : 'dog'}
great_dane = {'name' : 'great dane',
    'master' : 'diana',
    'type' : 'dog'}
labrador_dog = {'name' : 'labrador dog',
    'master' : 'dean',
    'type' : 'dog'}
border_collie ={'name' : 'border collie',
    'master' : 'ani',
    'type' : 'dog'}
pets = [golden_retriver, great_dane, labrador_dog, border_collie]

for pet in pets:
    print("Dog Name: " + pet['name'].title())
    print("\tmaster: " + pet['master'].title())
    print("\ttype: " + pet['type'].title())
