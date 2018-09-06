# 비슷한 객체의 딕셔너리
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
"""
하나의 딕셔너리에는 여러 객체의 정보를 저장할수 있다
보다시피 여기에서는 딕셔너리 하나를 여러 행에 나눠 썼다 각 키는 설문조사에
응답한 사람 이름이며 각 값은 그들이 선택한 언어이다. 딕셔너리를 정의할 때 여러 행이
필요하다면 여는 중괄호({) 다음에 엔터를 누른다 다음 행을 한 수준(공백 네 칸)
들여 쓰고, 첫 번째 키-값 쌍을 쓴 다음 쉼표를 쓴다, 여기서부터는 엔터를 누를 때마다
텍스트 에디터에서 자동으로 키-값 쌍을 첫 번째 키-값 쌍과 수준으로 들여 쓸것이다
"""
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".\n")
"""
favorite_language['sarah']로 sarah가 선택한 언어를 찾아내는 문법이다
print 문을 여러 행으로 나눠 쓰는 방법도 나타나있다 print라는 언어는
대부분 딕셔너리 이름보다 짧으므로 출력할 첫 번째 부분을 위에처럼 괄호 다음에
쓰는 게 좋다 엔터를 누르고 탭을 누러서 그다음의 모든 행을 print 문보다 한 수준 더
들여  써야한다
"""
for name, language in favorite_languages.items():
    print(name.title() + "s favorite language is " +
        language.title() + ".")
"""
위의 코드는 딕셔너리의 각 키-값 쌍에 루프를 실행한다 각 쌍을 처리할 때마다 키는
name변수에, 값ㅇ느 language 변수에 저장된다
"""
# 딕셔너리의 모든 키에 루프 실행하기
for name in favorite_languages.keys():
    print('\n' + name.title())
"""
딕셔너리의 값이 필요 없을 때는 keys() 메서드를 유용하게 쓸 수 있다
"""

friends = [ 'phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi  " + name.title() + " I see your favorite languages is " +
        favorite_languages[name].title() + "!")
"""
위에서 메시지를 출력 하고 싶은 친구 리스트를 따로 만들었다 루프 안에서는 각 사람
이름을 출력한다 그리고 if 문에서 name의 현재 값이 firends 리스트에 들어 있는지
체크한다 들어 있다면 친구들이 선택한 언어를 포함해 특별한 환영 메시지를 출력한다
마지막[name]은 딕셔너리에 name의 현재 값을 딕셔너리 키로 써서 좋아하는 언어에 접근
했다
"""
if 'erin' not in favorite_languages.keys():
    print("\nErin please take our poll!")
# keys() 메서드를 통해 특정 인물이 설문에 참여했는지 확인할 수도 있다

# 딕셔너리 키에 순서대로 루프 실행하기

for name in sorted(favorite_languages.keys()):
    print(name.title() + " thank you for taking the poll.")

"""
위의 for 문은 dictionary.keys() 메서드를 sorted() 함수로 감쌌다는 것을 제외하면
다른 for문과 같다 파이썬은 딕셔너리의 모든 키를 리스트로 만들고, 루프 실행 전에
그 리스트를 정렬한다 결과를 보면 설문에 참여한모든 사람이 순서대로 나타난다
"""

# 딕셔너리의 모든 값에 루프 실행하기

print("The following languages have been mentioned.")
for language in favorite_languages.values():
    print(language.title())
# 딕셔너리의 저장된 값에 흥미가 있다면 values() 메서드를 써서 키 값 리스트만
# 얻을 수 있다
print('\n')
for language in set(favorite_languages.values()):
    print(language.title())
"""
값이 적으면 문제가 없지만, 참가자 가 많은 설문이라면 반복이 심한 리스트를 얻는다
선택된 각 언어를 반복 없이 얻으려면 set를 사용한다 set는 리스트와 비슷하지만,
set의 각 항목은 반드시 단 하나만 존재한다
중복된 항목이 있는 리스트를 set()로 감싸면 파이썬은 리스트에서 항목을 단 하나씩만 꺼내
세트를 만든다
"""
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
"""
좋아하는 프로그래밍 언어 예제에서 각 사람의 응답을 리스트에 저장했다면
사람들은 좋아하는 언어를 하나 이상 선택할 수가 있었을 것이다 그 딕셔너리에 루프를
실행하면 각 사람에 연결된 값은 언어 하나가 아니라 언어 리스트였을 것이다 딕셔너리의
for 루프 안에서 다시 for 루프를 실행해 각 사람에 연결된 언어 리스트를 순회하자
"""
