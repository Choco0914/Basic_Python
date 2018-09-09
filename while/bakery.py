sandwich_orders = ['Club Sandwich', 'Chicken Salad Sandwich',
        'Submarine Sandwich', 'BLT Sandwich', 'Tuna Sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    print("I made a " + sandwiches.title())
    finished_sandwiches.append(sandwiches)

print("\nCompleted sandwich list:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title())
