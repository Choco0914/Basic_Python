# 관리자에게 인사
users = ['apple', 'computer', 'google', 'microsoft', 'amazon', 'admin']
for user in users:
    if user == 'admin':
        print(user + "님 안녕하세요, 상태 보고서를 보시겠습니까?\n")
    else:
        print(user + "님 안녕하세요, 다시 로그인 해주셔서 감사합니다.\n")
# 사용자 없음
users= []
if users:
    for user in users:
        print(user + " Hello")
else:
    print("사용자가 있어야 합니다!")
# 사용자 이름 체크(비교할때는 대소문자를 구별하지말자)
current_users = ['apple', 'computer', 'google', 'microsoft', 'amazon', 'admin']
new_users = ['banana', 'desk', 'GOOGLE', 'AMAZON', 'note']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " is already used, please change another name\n")
    else:
        print(new_user + "is possible to use!\n")
# 순번
"""
순번은 1st나 2nd 처럼 리스트에서의 위치를 나타낸다 1, 2, 3을 제외한 대부분의 순번은
th로 끝난다
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2ed")
    elif number == 3:
        print("3rd")
    elif number == 4:
        print("4th")
    elif number == 5:
        print("5th")
    elif number == 6:
        print("6th")
    elif number == 7:
        print("7th")
    elif number == 8:
        print("8th")
    elif number == 9:
        print("9th")
