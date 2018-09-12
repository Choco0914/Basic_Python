# 샌드위치
"""
고객이 샌드위치에 넣고 싶어하는 재료 리스트를 받는 함수를 만들자. 이 함수에는
함수 호출에서 제공하는 항목을 모두 수집하는 매개변수가 있어야 하고, 주문받은
샌드위치를 요약해서 출력해야 한다. 함수를 세 번 호출하고 그 때매다 다른 숫자의
매개변수를 넘겨라.
"""
def make_sandwich(number, *sandwich_list):
    print("Making " + str(number)+ " sandwich with the following ingredients:")
    for sandwich in sandwich_list:
        print("- " + sandwich)

make_sandwich(1, 'tomato', 'ham', 'photato')
make_sandwich(2, 'cow leg', 'onion', 'mushrooms')
make_sandwich(3, 'bacon', 'egg', 'beans')
