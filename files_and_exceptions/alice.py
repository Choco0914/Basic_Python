# FileNotFoundError 예외 처리
"""
파일로 작업할 때 흔히 일어나는 문제는 파일이 없는 문제이다. 원하는 파일이 다른 위치에
있을 수도 있고, 파일 이름에 오타가 있을 수도 있고, 그런 파일이 아예 존재하지 않을
수도 있다. 이런 상황은 모두 try-except 블록으로 단순하게 처리할 수 있다.

filename = 'alice.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
위와 같은 코드를 실행시키면 파이썬은 다음과 같은 트레이스백을 표시한다.
Traceback (most recent call last):
  File "alice.py", line 5, in <module>
    with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
"""
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " dose not exist."
    print(msg)

# 텍스트 분석
"""
책 전체가 들어 있는 텍스트 파일도 분석할 수 있다. 고전 문학 중 상당수는 공개되어
있으므로 단순한 텍스트 파일로도 이용할 수 있다. 이 섹션에서 사용하는 텍스트는
구텐베르크 프로젝트(http://gutenberg.org/)에서 가져왔다. 구텐베르크 프로젝트는
공개된 문학 작품을 모아서 관리하고 있으며, 프로그래밍 프로젝트에 문학 텍스트를 사용할
생각이 있다면 훌륭한 자원이다.

이상한 나라의 엘리스(Alice in wonderland)의 텍스트를 가져와서 텍스트에 들어 있는
단어 숫자를 세어보자. 문자열에서 단어 리스트를 만드는 문자열 메서드 split()을
이용할 것이다. 제목인 Alice in Wonderland만 들어 있는 문자열에 split()을
사용해보자
"""
title = "Alice in wonderland"
print(title.split())
"""
split() 메서드는 공백을 기준으로 문자열을 분리하고 각 부분을 리스트에 저장한다.
결과는 문자열을 구성하고 있던 단어 리스트이며, 일부 단어에는 구두점이 들어 있을 수도
있다. 이상한 나라의 엘리스의 텍스트 전체에 split()을 써서 단어 숫자를 세겠다.
그리고 리스트 항목을 세면 텍스트에 들어 있는 단어 숫자를 대략 알 수 있다.
"""
filename = 'alice.txt'

try:
    with open('text_files/' + filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " dose not exist."
    print(msg)
else:
    # 파일에 들어 있는 단어를 센다.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename  + "has about " +str(num_words) + "words.")
