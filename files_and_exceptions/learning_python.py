# 파이썬 배우기
"""
텍스트 에디터에서 빈 파일을 만들고 지금까지 파이선에 대해 배운 내용을 몇 줄로
요약하자. 각 행은 파이썬은 이런 일을 할 수 있다라는 구절로 시작하자. 이 파일을
이 장의 연습무넺와 같은 폴더에 learning_python.txt라는 이름으로 저장해라.
이 파일을 읽고 당신이 배운 내용을 세 번 출력하는 프로그램을 만들자. 한 번은
파일 전체의 콘텐츠를 출력하는 방법, 한 번은 파일 객체에 루프를 실행하는 방법,
한 번은 리스트에 저장하고 with 블록 밖에서 출력하는 방법을 쓰자.
"""

filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
