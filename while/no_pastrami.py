sandwich_orders = ['Club Sandwich', 'pastrami', 'Chicken Salad Sandwich',
        'Submarine Sandwich', 'BLT Sandwich', 'pastrami', 'Tuna Sandwich',
        'pastrami',]
print("\nThere is not pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
