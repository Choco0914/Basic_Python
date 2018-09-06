# 딕셔너리 안에 리스트 담기
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza" +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
