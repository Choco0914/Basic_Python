requested_topping = 'mushrooms'
if requested_topping != 'achovies':
    print("Hello the achovies!")
"""
requested_topping의 값과 'anchovies'를 비교한다. 이들 값이 일치하지 않으면
파이썬은 True를 반호나하고 if 문의 다음의 코드를 실행한다 두 값이 일치하면 파이썬은
False를 반환하고 if 문 다음의 코드를 실행하지 않는다
"""
# 여러 조건테스트 하기
"""
if-elif-else 문은 강력하지만 통과 조건이 단 하나일 때만 어울린다
파이썬은 한 가지 테스트가 통과하는 즉시 다른 테스트는 모두 건너뛴다 이런 방식은
효율적이며 특정 조건 한가지만 테스트할 수 있다는 장점이 있다

하지만 원하는 조건을 모두 체크 할 때도 있다 이럴때는 elif나 else 블록 없이
단순한 if문을 여러 개 써야한다 이런방법은 조건이 하나 이상 True일 수도있고, Ture인
조건마다 어떤 동작을 해야 할때도 있다
"""
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding cheese")

print("\nFinished making your pizza!")
"""
위의 코드르 만약 if-elif-else 문을 이용해 만들었다면 첫번째 에서 통과되어 밑의 코드
블록은 무시되어 실행하지 않는다
"""
# 리스트에서 if 문 이용하기
requested_toppings = ['mushrooms', 'green pepeers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green pepeers':
        print("Sorry we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!\n")
"""
예르들어 피자가게에서 요구된 topping이 있는데 맞는 재료가 없다면 for 루프안에
if 문을 써서 효율적으로 처리할수 있다
먼저 주문받은 항목을 피자에 추가하기 전에 재료가 있는지 확인하고 없으면 피망이
떨어졌다는 메세지를 출력한다 else 블록을 썻으므로 다른 토핑은 모두 피자에 추가된다
"""
# 리스트가 비어 있지 않은지 확인하기
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
"""
이제 곧 사용자에게서 정보를 받아 리스트에 저장할 텐데 루프를 실행할 때 리스트에
항목이 항상 있다고 확신할 수 없다. 이런 상황에서for 루프를 쓰기 전에 리스트가 비어
있지는 않은지 체크하는 게 좋다
"""
# 여러 리스트 다루기
available_toppings = ['mushrooms', 'olives', 'green peppers',
                       'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
"""
위에서 available_toppings리스트에 피자 전문점에서 준비된 토핑 리스트를 정의했다
이 피자 전문점에서 실행할 토핑이 일정하다면 튜플을 쓸 수 있다
그리고 requested_toppings에 고객이 요청한 토핑 리스트를 만들었다
available_toppings에 없는 'french fries'가 안에 들어있다 그리고 for loop에
주문받은 토핑 리스트를 실행한다 루프 안에 있는 if문에서는 먼저 주문받은 각 토핑이
준비된 토핑 리스트에 있는지 체크한다 준비된 토핑이 리스트에 있다면 토핑을
피자에 추가한다 그렇지 않다면 else 블록이 실행한다
"""
