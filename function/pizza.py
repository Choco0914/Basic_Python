# 매개변수를 임의의 숫자만큼 전달하기
def make_pizza(*toppings):
    """주문받은 토핑 리스트 출력"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
"""
이따금 핫무가 매개변수를 몇 개나 받을지 미리 알 수 없을 때도 있다.
다행히 파이선에서는 함수가 임의의 숫자만큼 매개변수를 받도록 정의하는 방법이 있다.

피자 만드는 함수를 예로 들겠다. 이 함수는 여러 가지 토핑을 받지만, 고객이 토핑을
몇 개 주문할지 미리 알 수는 없다.
매개변수 이름 *toppings의 애스터리스크(*)는 파이썬이 빈 튜플 toppings를
만들고 받는 값을 모두 이 튜플에 저장하라는 의미이다. 함수 바디의 print 문은
파이썬이 값 하나인 호출과 값이 여럿인 호출을 처리할 수 있음을 보여준다.
다른 방식으로 호출해도 비슷하게 처리한다. 파이썬은 설령 함수에서 단
하나의 값만 받더라도 매개변수를 튜플로 묶는다.
"""
def make_pizza(*toppings):
    """만들려고 하는 피자를 요약한다."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 위치형 매개변수와 임의의 매개변수 함꼐쓰기
def make_pizza(size, *toppings):
    """만들려고 하는 피자를 요약한다."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'exra cheese')
