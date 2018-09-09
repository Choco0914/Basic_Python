vacation_places = []

active = True
while active:
    places = input("\nIf you could visit one place in the world" +
    "\nwhere would you go?")


    vacation_places.append(places)

    repeat = input("\nDo you have any more places to go? (yes/no)")
    if repeat == 'no':
        active = False
print("\nList of places you want to go on vacation:")
for vacation in vacation_places:
    print("\t" + vacation.title())
