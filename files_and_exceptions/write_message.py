# 파일에 쓰기
filename = 'programming.txt'

with open(filename, 'w') as file_object:    # ...1
    file_object.write("I love programming.")    # ...2
"""
1 행에서 open()을 호출하면서 매개변수 두 개를 넘겼다. 첫 번째 매개변수는 여전히
파일 이름이다. 두 번째 매개변수 'w'는 이 파일을 쓰기 write 모드로 열라는 뜻이다.
파일을 열 때는 읽기(read) 모드 ('r'), 쓰기 모드('w'), 이어붙이기(attend) 모드('a'),
읽고 쓰기 모드('r+')를 쓸수 있다. 모드 매개변수를 생략하면 파이썬은 기본적으로 파일을
읽기 모드로 연다.

2에서는 파일 객체에 write() 메서드를 실행해 문자열을 파일에 썼다. 이 프로그램에는
터미널 출력이 없지만, programming.txt 파일을 열면 한 행을 볼 수 있다.
"""
# 여러 행 쓰기
filename = 'programming.txt'

with open(filename, 'w') as file_object:    # ...1
    file_object.write("I love programming.")    # ...2
    file_object.write("I love creating new games.")
"""
write() 함수는 텍스트에 줄바꿈 문자를 추가하지 않는다. 따라서 두 행 이상을 쓰면서
줄바꿈 문자를 쓰지 않으면 파일이 원하는 대로 보이지 않을 수 있다.
"""
filename = 'programming.txt'

with open(filename, 'w') as file_object:    # ...1
    file_object.write("I love programming. \n")    # ...2
    file_object.write("I love creating new games. \n")
"""
write() 문에 줄바꿈 문자(\n)을 넣으면 각 문자열이 한 행이 된다.
터미널에서 출력할 때와 마찬가지로 공백과 탭 문자, 빈 행을 써서 출력 형식을 잡을 수
있다.
"""
# 파일에 이어 붙이기
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets. \n")
    file_object.write("I love creating apps that can run in a browser. \n")
"""
기존 내용을 덮어쓰지 않고, 파일에 내용을 추가하라면 파일을 이어붙이기 모드로 열 수
있다. 파일을 이어붙이기 모드로 열면 파이썬은 파일 객체를 반환하기 전에 파일을 지우지
않는다. 파일에 쓰는 행은 모두 파일 마지막에 추가된다. 파일이 존재하지 않으면 파이썬이
빈 파일을 새로 만든다.
"""
