"""
표준 딕셔너리로 용어 사전을 OrderedDict 클래스를 써서 이 프로그램을
출력 순서가 키-값 쌍을 딕셔너리에 추가한 순서와 같은지 확인하자.
"""
from collections import OrderedDict

language_dictionary = OrderedDict()

language_dictionary['주석'] = '실행되지 않는 코드'
language_dictionary['리스트'] = '순서가 있는 목록'
language_dictionary['if문'] = '조건 테스트'
language_dictionary['딕셔너리'] = '키-값 쌍인 코드'
language_dictionary['메서드'] = '클래스로 만든 데이터를 다루기위한 함수'
language_dictionary['for 문'] = '코드들을 어떤 기준까지 반복 실행한다.'
language_dictionary['루프'] = '어떠한 행동들을 반복해주는 행동.'
language_dictionary['불리언'] = '어떤 조건표현식을 평가하고 True와 False로 나타낸다'

for language, description in language_dictionary.items():
    print("\nLanguage: " + language)
    print("Decription: " + description)
