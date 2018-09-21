# 좋아하는 숫자
"""
사용자가 좋아하는 숫자를 묻는 프로그램을 만드세요. json.dump()를 써서 숫자를 파일에
저장하자. 별도의 프로그램을 만들어 이 값을 묻고 "당신이 좋아하는 숫자는 ___입니다."
같은 메시지를 출력하자.

숫자가 이미 저장됐다면 좋아하는 숫자를 사용자에게 보고하자. 그렇지 않다면 사용자가
좋아하는 숫자를 묻고 파일에 저장하자. 프로그램을 두 번 실행해 잘 동작하는지 확인해라.
"""
import json

def get_stored_numbers():
    """사용자가 좋아하는 숫자를 저장한다."""
    filename = 'favorite_numbers.json'
    try:
        with open(filename) as f:
            numbers = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return numbers

def favorite_number():
    favorites = get_stored_numbers()
    """사용자가 좋아하는 숫자를 보여준다."""
    filename = 'favorite_numbers.json'
    if favorites:
        print(favorites + " is your favorite number!")
    else:
        with open(filename, 'w') as f:
            what_numbers = input("What is your favorite number? ")
            numbers = json.dump(what_numbers, f)
            print("We'll rememver" + what_numbers + "!")

favorite_number()
