# if문
age = 19
if age >= 18:
    print("You are old enough to vote!")
# python은 age의 값이 18보다 크거나 같은지 체크한다 age의 값은 18보다 크므로
# 파이썬은 들여 쓴 print문을 실행한다
    print("Have you registered to vote yet?\n")
# if-else 문
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registerd to vote yet?")
else:
    print("Sorry, You are too young to vote. ")
    print("Please register to vote as soon as you turn 18!")
"""
만약 조건 테스트가 통과하지 못하면 다른 동작을 해야할 때가 있다 이럴때는 파이썬의
if-else 문을 사용한다 if-else 블록은 if 문과 비슷하지만 else 문은 주곤 테스트가
실패했을 때 실행할 동작을 정의한다
이번에는 age가 18미만이므로 조건 테스트는 실패하고 else 블록의 코드가 실행한다
"""
