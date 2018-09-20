# 예외
"""0으로 나눈 에외 처리"""
# print(5/0)
"""
위와 같은 5를 0으로 나눈 값을 출력하라는 코드를 실행시키면 다음과 같은 트레이스백을
파이썬이 표시한다.
Traceback (most recent call last):
  File "division.py", line 3, in <module>
    print(5/0)
ZeroDivisionError: division by zero
에러 ZeroDivisionError는 트레이스백이 보고한 예외 객체이다.
"""
# try-except 블록
"""
에러가 일어날 수 있다고 생각한다면 try-except 블록을 써서 가능성이 있는 예외를
처리할 수 있다. 파이썬이 어떤 코드를 실행하게 하고, 그 코드가 특정 예외를 일으켰을
때 어떻게 할지도 지시한다.
"""

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zeor!")

# 예외를 써서 충돌 막기
"""
정확한 에러 처리는 에러가 일어난 후에 프로그램이 할 일이 더 있을 때 중요하다.
사용자 입력을 받는 프로그램에서 이런 상황이 잦다. 프로그램이 잘못된 입력에 응답한다면
충돌하지 않고 올바른 입력을 요청할 수 있다.

나눗셈만 하는 단순한 계산기를 만들어 보자.
"""
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("second_number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
print("\n")

# else 블록
"""
에러를 일으킬 수 있는 행을 try-except 블록으로 감싸 이 프로그램을 에러에 더 강하게
만들 수 있다. 에러는 나눗셈을 하는 행에서 발생하므로 여기에 try-except 블록을 써야
한다. 이 예제에는 else 블록도 들어 있다. try 블록이 성공적으로 실행돼야만 실행할
코드는 모두 else 블록에 들어간다.
"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
