toppings = "What pizza toppings do you want?"
toppings += "\n(If you don't need toppings "
toppings += "plese enter 'quit' to end the program) "
topping = ""

while topping != 'quit':
    topping = input(toppings)
    if topping != 'quit':
        print(topping)
