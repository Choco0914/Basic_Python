filename = 'guest.txt'

guests = []
guests_exit = True
guest_question = "\nWhat is your name? "
guest_question += "\n(Enter 'quit' when you are finished.)\n"
while guests_exit:
    guest = input(guest_question)
    if guest == 'quit':
        guests_exit = False
    else:
        guests.append(guest)
with open(filename, 'w') as file_object:
    for guest in guests:
        file_object.write(guest + "\n")
