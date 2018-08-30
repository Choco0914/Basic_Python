players = ['charles', 'martina', 'MICAEL', 'florence', 'eli']
print('eli' == players[-1])
print('micael' == players[2].lower())
big = 28
baby = 21
print(big == baby)
print(big > baby)
print(big >= baby)
print(big <= baby)
print(big >= 22 and baby >= 22)
print(big >= 22 or baby >= 22)
player = 'Jordan'
if player in players:
    print(player)
if player not in players:
    print("not human")
