# 파일 콘텐츠 다루기
filename = 'pi_digits.txt'

with open('text_files/' + filename) as file_object:
    lines = file_object.readlines()

pi_string = ''   # ....1
for line in lines:  # ...2
    pi_string += line.strip()

print(pi_string)    # ...3
print(len(pi_string))
"""
1에서는 파이(pi)숫자를 저장할 pi_string 변수를 만들었다. 그리고 2에서 루프를
실행해 각 숫자 행을 pi_string에 추가하고 줄바꿈 문자를 제거했다. 3에서는 이 문자
열을 출력해 문자열이 얼마나 긴지 봤다.

파이썬은 텍스트 파일을 읽을 때는 모든 텍스트를 문자열을 해석한다. 숫자를 읽고
그 값을 숫자로 쓰고 싶다면 int() 함수를 써서 정수로 바꾸거나 float() 함수를
써서 부동소수점 숫자로 바꿔라.
"""
# 백만 단위의 큰 숫자 다루기
filename = 'pi_million_digits.txt'

with open('text_files/' + filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

# pi에 나의 생일이 들어 있을까?
filename = 'pi_million_digits.txt'

with open('text_files/' + filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not apper in the first million digits of pi.")
