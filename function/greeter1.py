# 함수에서 while 루프 사용하기
def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환한다."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
# 이건 무한 루프이다!
# while True:
#    print("\nPlease tell me your name: ")
#    f_name = input("First name: ")
#    l_name = input("Last name: ")
#
#    formatted_name = get_formatted_name(f_name, l_name)
#    print("\nHello, " + formatted_name + "!")
"""
위의 코드는 중간 이름을 받지 않은 get_formatted_name()의 단순한 버전을 사용했다.
while 루프는 사용자에게 이름을 요청하고, 성과 이름을 묻는 프롬프트(Please tell me
your name: )을 표시한다.
하지만 위 프로그램은 문제가 있다. while 루프에서는 종료 조건이 없다 입력을
여러 번 받는다면 종료 조건을 어딘가에 있어야 한다. 사용자가 가능한 쉽게 빠져나갈수
있어야하므로 각 프롬프트 마다 나갈 수 있는 방법이 있어야 한다. break 문을 쓰면 어떤
프롬프트 에서든 쉽게 루프를 나갈 수 있다.
"""
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
