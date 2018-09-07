# int()를 써서 숫자형 입력받기
"""
>>> age = input("How old are you?")
How old are you?27
>>> age
'27'
파이썬은 input() 함수로 입력받은 내용은 모두 문자열로 간주한다
프로그램에서 사용자의 입력을 요청한다면 입력 후 반드시 엔터를 눌러야 한다
숫자가 따옴표로 둘러쌓여 있는걸 보고 우리는 파이썬이 숫자를 문자열로 반환했다는것을
알수있다
>>> age >= 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int'
입력된 나이를 숫자와 비교하려 하면 파이선은 문자열과 정수를 비교할 수 없으므로
위와 같은 에러르 일으킨다. age에 저장된 '21'은 문자열로 간주하므로 숫자와 비교할 수
다 이럴때 입력을 숫자로 바꾸는 int() 함수로 이 문제를 해결 할 수 있다.
int() 함수는 숫자의 문자열 표현을 숫자형 표현으로 바꿔준다

>>> age = input("How old are you? ")
How old are you? 27
>>> age = int(age)
>>> age >= 18
True
프롬프트에 27을 입력하면 파이썬이 숫자를 문자열로 해석하지만, int()가 그 값을
숫자로 바꾼다. 이제 age에 숫자 값 27이 들어가므로 age가 18보다 크거나 같은지
비교하는 조건 테스트를 할 수 있다
"""
