toppings = "What pizza toppings do you want?"
toppings += "\n(If you don't need toppings "
toppings += "plese enter 'quit' to end the program) "
topping = ""
active = True

while active:
    topping = input(toppings)
    if topping == 'quit':
        active = False
    else:
        print(topping)

topping = ""

while topping != 'quit':
    topping = input(toppings)

    if topping != 'quit':
        print(topping)

topping = ""

while True:
    topping = input(toppings)
    if topping == 'quit':
        break
    else:
        print(topping)
