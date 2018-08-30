pizzas = ['chesse pizza', '치즈크러스트피자', '포테이토피자' ]
friends_pizzas = pizzas[:]

pizzas.append('불고기 피자')
friends_pizzas.append('시카고 피자')

print("\n내가 좋아하는 피자는")
for pizza in pizzas:
    print(pizza)
print("\n내 친구가 좋아하는 피자는")
for friend_pizza in friends_pizzas:
    print(friend_pizza)
