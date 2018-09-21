# 사용자가 생성한 데이터 저장하고 읽기
import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)     # ...1
    print("Welcome back, " + username + "!")    # ...2

"""
1에서 json.load()를 썻 username.json에 저장된 정보를 username 변수로 읽어 들였다.
이제 사요앚 이름을 확인했으니 2처럼 환영할 수 있다.
"""
