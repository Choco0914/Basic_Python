customers = "How old are you?"
customer = ""

while customer == "":
    customer = input(customers)
    if int(customer) < 3:
        print("You are free!")
    elif 3 <= int(customer) <= 12:
        print("Ticket price is $ 10")
    else:
        print("Ticket price is $ 15")
