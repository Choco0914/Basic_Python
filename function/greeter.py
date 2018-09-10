# 함수 정의
def greet_user():
    """간단한 환영 인사를 표시한다"""
    print("Hello!")

greet_user()
"""
위의 코드는 함수의 가장 간단한 구조이다. 첫번째 행의 키워드 def는 파이썬에게 지금부터
함수를 정의한다고 알린다. 첫번째 행은 이름과(필요하다면)함수에 어떤 정보가 필요한지
알리는 함수 정의이다. 필요한 정보는 괄호 안에 쓴다. 여기서 함수 이름은 greet_user()
이며 추가 정보는 필요 없으므로 괄호는 비어 있다. 추가 정보가 없더라도 괄호 자체는
함께 서야 한다. 함수 정의는 콜론으로 끝난다.

def greet_user(): 다음의 들여 쓴 행은 모두 함수의 바디(body)이다. 두번째의
쌍따옴표 세개로 묶여진 코드는 도큐멘트 스트링(document string) 혹은
독스트링(docstring)이라 불리는 주석이다 함수가 무슨 일을 하는지 설명하는 주석이다
파이썬에서 프로그램 문서를 만들때는 따옴표 세 개로 둘러 싸인 독스트링을 사용한다.
"""
# 함수에 정보 전달
def greet_user(username):
    """간단한 환영 인사를 표시한다"""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
"""
함수 정의인 def greet_user()의 괄호 안에 username을 넣어 이름을 받아오겠다.
이제 함수는 자신을 호출할 때마다 username의 값을 받을 거라고 예상한다
greet_user('jesse')는 greet_user()를 호출하면서 print 문에 필요한 정보를 넘긴다.
함수는 당신이 제공한 이름을 받아서 환영 인사를 한다
마찬가지로 greet_user('sarah')를 실행하면 greet_user()를 호출하면서 'sarah'를
넘기고 'Hello, Sarah'를 출력하게 된다. 원할 때맏 greet_user()를 호출하고
예층 가능한 결과를 얻을 수 있다.

greet_user()의 정의에서 변수 username을 매개변수(parameter)라고 한다.
매개변수는 함수가 작업하기 위해 필요한 정보이다. greet_user('jesse')의 'jesse' 역시
매개변수(argument)이다. 함수를 호출할 때 전달하는 값도 매개변수라고 부른다.
함수를 호출할 때는 함수가 사용하길 원하는 값을 괄호 안에 넣는다. 여기서는
매개변수 'jesse'가 함수 greet_user()에 전달됐고 변수 username에 저장됐다.
"""
