# 1. 정수
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
# 파이썬에서는 정수를 더하고 빼고, 곱하고, 나눌수 있다 화면에 출력하려며 print() 이용
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)
# 곱하기 기호를 두개를써서 제곱을 표현할수 있다
print(2 + 3*4)
print((2 + 3) * 4)
"""
파이썬은 계산 순서도 지원한다 표현식 하나에서 계산을 여러번 할수있고
또 괄호를 써서 임의로 계산순서를 지정할 수도 있다
위의 예제에서 공백은 파이썬이 코드를 해석할 때 아무 영향을 주지않는다
"""
# 2. 부동소수점 숫자
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
# 가끔 이상한 답이 나올수가 있다
print(0.2 + 0.1)
print(3 * 0.1)
"""
파이썬은 될  있으면 결과를 정확하게 나타내려한다 이문제는 컴퓨터가 내부적으로
숫자를 다루는 방식 때문에 일어난 것이다 지금은 신경쓰지 말자
"""
# 3. str() 함수를 이용해 타입 에러 피하기
# 변숫값을 메시지 안에 쓰일때가 있는데 예를들어 누군가의 생일을 축하한다고 가정하자
age = 23
message = "Happy " + str(age) + "rd Brithday!"

print(message)
"""
위의 코드를 실행하면 다음과 같은 에러를 보여준다
Traceback (most recent call last):
  File "숫자(number).py", line 32, in <module>
    message = "Happy" + age + "rd Birthday!" ...1
    TypeError: must be str, not int
이 에러는 타입 에러이다 타입에러는 우리가 사용하려는 정보를 잘못 연결했을 때 파이썬
이 보내는 신호이다 1 에서 파이썬은 정수(int)값을 문자열(str)과 연결할 수 없다고
설명한다 우리는 상황에 따라 23을 숫자나 문자로 인식하지만 파이썬에게는 명시적으로
알려줘야한다 이때 str() 함수를 사용하면 문자열이 아닌 값을 문자열로 변환할수 있다
"""
# Practice!
favorite_number = 77
favorite_number = "My favorite number is " + str(favorite_number)
print(favorite_number)
