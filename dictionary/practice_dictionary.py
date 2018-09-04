language_dictionary = {'주석' : '실행되지 않는 코드',
                '리스트' : '순서가 있는 목록',
                'if문' : '조건 테스트',
                '딕셔너리' : '키-값 쌍인 코드',
                '메서드' : '클래스로 만든 데이터를 다루기위한 함수',
                'for 문' : '코드들을 어떤기준까지 반복실행한다',
                '루프' : '어떠한 행동들을 반복해주는 행동이다',
                '불리언' : '어떤 조건표현식을 평가하고 True와 False로 나타낸다',}

for language, description in language_dictionary.items():
    print("\nLanguage: " + language)
    print("Decription: " + description)

# River

rivers = {'rhine' : 'germany',
        'yangtze' : 'china',
        'mississippi' : 'canada',}
for river, country in rivers.items():
    print(river.title() + ' is in ' + country.title())
print("\n")
for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
poll_people = ['jen', 'tim', 'sarah']

for poll in poll_people:
    if poll in favorite_languages:
        print(poll + ", Thank you\n")
    else:
        print(poll +", you need to poll")
