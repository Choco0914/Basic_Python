# 사용자가 생성한 데이터 저장하고 읽기

import json

# 사용자 이름이 저장됐다면 불러온다.
# 그렇지 않다면 사용자 이름을 묻고 저장한다.

def get_stored_username():
    """저장된 사용자 이름이 있다면 불러온다."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except JSONDecodeError:
        return None
    else:
        return username

def get_new_username():
    """새 사용자 이름을 묻는다."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def check_username():
    """현재 사용자가 마지막 사용자인지 확인한다."""
    username = input("What is your name? ")
    username = username.lower()
    filename = 'username.json'
    with open(filename) as f_obj:
        usernames = json.load(f_obj)
        usernames = usernames.lower()
        usernames = usernames.split()
    for get_username in usernames:
        if username == get_username:
            return get_stored_username()
        else:
            print("You are not registered Please Register!")
            check = input("Do you want to register your name? (y/n)")
            if check == 'y':
                username = get_new_username()
                print("We'll remember you when you come back, " +
                 username + "!")

def greet_user():
    """사용자를 이름으로 환영한다."""
    username = check_username()

    if username:
        print("Welcome back, " + username + "!")

greet_user()
