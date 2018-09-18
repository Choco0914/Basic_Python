# 파일 전체 읽기와 파일 경로
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 한 행씩 읽기
filename = 'pi_digits.txt'

with open('text_files/' + filename) as file_object:
    for line in file_object:
        print(line.rstrip())
# 파일에서 행 리스트 만들기
filename = 'pi_digits.txt'

with open('text_files/' + filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print(lines)
"""
단순히 파일 콘텐츠를 출력하기만 할 뿐이라도 먼저 파일을 열어야 접근할수 있다.
open() 함수는 열어야 하는 파일 이름을 매개변수를 받는다.
파이선은 이 파일을 현재 실행 중인 프로그램이 저장된 폴더에서 찾는다.
위의 에제에서는 file_reader.py가 현재 실행중 이다. 그러므로 파이썬은 file_reader.py
가 저장된 폴더에서 pi_digits.txt 파일을 찾는다. 열려는 파일이 다른 폴더에 있으면
경로를 지정해줘서 파일을 열어줘야 한다. open()함수는 파일을 나타내는 객체를 반환한다.
그리고 파이선은 이 객체를 file_object에 저장한다.

파일을 열면(open()) 작업을 마친 후에는 반드시 파일을 닫아야(close()) 한다. 그런데
이 프로그램에서는 clsoe()를 사용하지 않았다. with를 쓰면 프로그램에서 그 파일을 더는
사용하지 않을 때 파이썬이 알아서 파일을 닫는다.
프로그래머가 직접 close()로 파일을 닫을 수도 있지만, 프로그램에 버그가 있거나
깜빡 잊어서 close() 문이 실행되지 않으며 파일이 닫히지 않는다. 파일을 제대로 닫지
않으면 데이터를 잃거나 망칠 수 있다. 그리고 close()를 너무 일찍 호출하면 닫힌, 즉
접근할 수 없는 파일에 접근을 시도해 에러가 더 많이 생길 수 있다. 파일을 언제
닫을지 정확히 판단하는 건 쉽지 않지만, with 문을 쓰면 파이썬이 판단한다.
우리는 파일을 열고 원하는 대로 작업하면서 파이썬이 적당한 시접에 파일을 닫을 거라고
믿기만 한다.

with() 문을 쓰면 open()이 반환한 파일 객체는 with 블록 안에서만 쓸 수 있다.
with 블록 밖에서도 파일 콘텐츠에 접근하려면 블록 안에서 파일 행들을 리스트에 저장하고
그 리스트로 작업하면 된다. 
"""
