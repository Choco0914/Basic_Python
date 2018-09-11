# 딕셔너리 반환하기
def build_person(first_name, last_name):
    """사람에 관한 정보 딕셔너리를 반환한다."""
    person = {'first':'first_name', 'last':'last_name'}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
"""
함수는 어떤 타입의 값이라도 반환할 수 있다. 따라서 함수는 단순한 값 외에도 리스트와
딕셔너리처럼 더 복잡한 데이터 구조도 반환할 수 있다. 예를 들어 위의 함수는 이름의
각 부분을 받고 그 사람을 나타내는 딕셔너리를 반환한다.
"""
def build_person(first_name, last_name, age=''):
    """사람에 관한 정보 딕셔너리를 반환한다."""
    person = {'first':'first_name', 'last':'last_name'}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
"""
위 함수는 단순한 텍스트 정보를 받아 더 의미 있는 데이터 구조에 넣으므로 단순히
출력만 하는 게 아니라 더 많은 일을 할 수 있다. 문자열 'jimi' 와 'hendrix'는
이제 이름과 성으로 분류됐다. 이 함수를 쉽게 확장해 중간 이름이나 나이, 직업, 기타
그 사람에 관해 저장하고 싶은 정보를 받게끔 만들 수 있다.
"""
