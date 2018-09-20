# 흔한 단어
"""
구텐베르크 프로젝트를 방문해 분석해보고 싶은 텍스트를 몇 개 찾자. 텍스트
파일을 내려받거나 브라우저에서 텍스트를 복사해 텍스트 파일로 저장하자.

count() 메서드를 써서 단어나 구절이 문자열에 몇 번 나타났는지 알아볼 수 있다.
lower()를 써서 문자열을 소문자로 바꾸면 대소문자와 상관없이 원하는 단어를 찾을 수
있다.
구텐베르크 프로젝트에서 찾은 파일을 읽고 각 텍스트에 the가 몇 번 나타나는지 세는
프로그램을 만들자.
"""
filename = 'alice.txt'

with open('text_files/' + filename) as f:
    how_many = f.read()

how_many = how_many.lower()
print(how_many.count('alice'))
