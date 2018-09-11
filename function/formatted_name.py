# 반환값
def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환한다."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
"""
함수가 항상 결과를 직접 출력하지는 않는다. 출력하는 대신에 데이터를 처리하고 값을
반환할 수도 있따. 함수가 반환하는 값을 반환값이라 부른다. return 문은 함수 내부에서
값을 받고 그 함수를 호출한 행에 그 값을 반환한다. 반환값을 쓰면 프로그램에서 하는 일
대부분을 함수에 넣어 프로그램 본문을 단순화할 수 있다.

첫 번째 행에서 get_formatted_name() 함수가 성과 이름을 매개변수로 받도록 정의했다.
두 번째 행에서 함수는 성과 이름 사이에 공백을 두고 결합해서 full_name에 저장한다.
그리고 full_name의 단어 첫 글자를 대문자로 바꿔, 함수를 호출했던 return 문에
반환한다.
값을 반환하는 함수를 호출할 때는 반환값을 저장할 변수를 제공해야 한다.
여기서는 반환값을 musician 변수에 저장했다.
"""
# 매개변수를 옵션으로 만들기
def get_formatted_name(first_name, middle_name, last_name):
    """읽기 쉬운 전체 이름을 반환한다."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
"""
이따금 매개변수를 옵션으로 만들어서 그 함수를 쓰는 사람들이 원할 때만 추가 정보를
제공하는 게 합리적일 수 있다. 매개변수에 기본값을 쓰면 옵션으로 만들 수 있다.
위 코드에서 중간이름이 늘 필요로 하기에 성과 이름만 써서 함수를 호출하면
제대로 동작하지 않는다. 그러면 불필요할 수도 있는 중간 이름을 옵션으로 만들어보는
방법이 있다
"""
def get_formatted_name(first_name, last_name, middle_name=''):
    """읽기 쉬운 전체 이름을 반환한다"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
