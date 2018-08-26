"This is a string. 문자열은 이렇게 표기한다"
# 큰따옴표로 처리한 문자열
'This is also a string. 이렇게도 표현할수있다'
# 작은 따옴표로 처리한 문자열
'I told my freind, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
"""
문자열에서 ''는 ""안에 속하면 문자로 인식하고
""도 마찬가지로 ''안에 속하면 문자로 인식되어진다
"""
# 1.대소문자 바꾸기
name = "ada lovelace"
print(name.title())
"""
print()안에 있는 title()은 메서드이다 메서드란 파이썬이 데이터 조각에 취하는
행동이다 name.title()에 있는 점(.)은 name변수에 title() 메서드를 작용하라는 뜻이다
메서드에는 종종 추가 정보가 필요하므로 ()안에 넣어서 알려준다 현재는 필요없어서
비워두었다 title()은 파일을 실행해보면 각 단어의 첫 글자를 대문자로 표시해준다
"""
print(name.upper())
print(name.lower())
"""
파일을 실행해보면 알겠찌만 upper()와 lower()메서드는 각각 단어를 대문자로 바꾸거나
소문자로 전부 바꿔버린다
"""
# 2.문자열 결합
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
# " "은 공백을 남겨두려 넣어주었다 없으면 단어가 붙어서 결합되어버린다
print(full_name)
"""
Python에서 문자열을 결합할때 더하기 기호(+)를 사용한다 이 예제에서는 first_name와
공백, last_name을 +로 결합했다 이렇게 결합하는 방법을 병합이라고 부른다
"""
print("Hello, " + full_name.title() + "!")
# title()메서드를 이용해 이름형식을 적절히 바꿨다

message = "Hello, " + full_name.title() + "!"
print(message)
# 변수로 만들어 전체 메시지를 출력할수도있다

# 3. 탭이나 줄바꿈 문자로 문자열에 공백 추가하기
print("Python")
print("\tPython")
# \t를 같이 쓰게되면 자동으로 tab효과를 적용할수있다
print("Language:\nPython\nC\nJavaScript")
# 행을 바꾸려면 문자 조합\n 을 사용한다 \n은 줄바꿈 문자이다
print("Language:\n\tPython\n\tC\n\tJavaScript")

# 4. 공백 잘라내기
favorite_language = 'python '
print(favorite_language)
"""
Python은 프로그래머가 따로 지시하지 않으면 공백을 문자열로 감지하게된다
웹사이트 로그인을 예로들면 패스워드가'python'인데 'python '이라고 입력하게되면
당연히 패스워드가 틀렸다고 하며 로그인이 되지 않는다 다행히 파이썬에서는
공백을 제거하는 쉬운 방법이 있다
"""
favorite_language = favorite_language.strip()
print (favorite_language)
"""
strip()을 이용하게 되면 양쪽 공백을 없애준다 ()안에 없애고 싶은 문자나 숫자를
넣게 되면 strip()메서드가 잘라내준다
rstirp()은 오른쪽 공백을 lstrip()은 왼쪽 공백을 잘라내준다
"""
# 5. 문자열에서 문법 에러 피하기
message1 = "One of Python's strengths is its diverse community."
print(message1)
"""
message1 = 'One of Python's strengths is its diverse community.'
만약 쌍따옴표가 아닌 따옴표로 위의 문장을 감쌀경우 아래와 같은 에러가 발생한다
  File "String(문자열).py", line 69
    message1 = 'One of Python's strengths is its diverse community.'
                              ^
SyntaxError: invalid syntax
"""
"""
에러는 다양한 원인으로 찾기가 힘들다 인터넷상에서 질문을 통해 에러의 원인을
알수도 있고 스스로 찾아서 해결할수도 있다 또한 인터넷에 본인과 같은 에러를 일으킨
사용자들이 있을것이다 그들이 올려놓은 질문의 답변들을 읽어보면 해결할수 있는 방법이
있을것이다
"""
