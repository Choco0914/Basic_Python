# 딕셔너리 안에 리스트 담기
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza" +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
"""
리스트를 딕셔너리 안에 넣는 게 유용할 때도 있따 예를 들어 누군가 주문한 피자를 어떻게
설명할지 생각해보자 리스트만 사용한다면 피자의 토핑 리스트밖에 저장하지 못한다
딕셔너리와 함께 사용하면 토핑 리스트가 당신이 설명하는 피자의 한 측면이 될 수 있다
딕셔너리 키 중 하나는'crust'이고 연결된 값은 문자열 'thick'이다
다음 키 'toppings'는 주문받은 토핑 전체를 지정한 리스트 이다 피자를 만들기 전에
주문 내용을 요약했고, 토핑을 출력할 for 루프를 만들었따 토핑 리스트에 접근하기 위해
'toppings'키를 사용하면 파이썬은 딕셔너리에서 토핑 리스트를 꺼낸다
"""
