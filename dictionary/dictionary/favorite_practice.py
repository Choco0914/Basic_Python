people = {'first name' : '순신',
    'last name' : '이',
    'age' : 53,
    'city' : '조선 한성부 건천동',}
print(people)

life_number = {'레오나르도 다빈치' : 67,
            '라파엘로' : 37,
            '미켈란젤로' :  89,
            '도나텔로' : 80,
            '고흐' : 37}
print('\n레오나르도 다빈치는 ' + str(life_number['레오나르도 다빈치']) +
    '년 살았다')
print('라파엘로 는 '+ str(life_number['라파엘로']) +
    '년 살았다')
print('미켈란젤로 는 ' + str(life_number['미켈란젤로']) +
    '년 살았다')
print('도나텔로 는' + str(life_number['도나텔로']) +
    '년 살았다')
print('고흐 는 ' + str(life_number['고흐']) +
'년 살았다')
# 용어사전
language_dictionary = {'주석' : '실행되지 않는 코드',
                '리스트' : '순서가 있는 목록',
                'if문' : '조건 테스트',
                '딕셔너리' : '키-값 쌍인 코드',
                '메서드' : '클래스로 만든 데이터를 다루기위한 함수'}

print("\n주석 : " + str(language_dictionary['주석']) +"\n" +
    "리스트 : " + str(language_dictionary['리스트']) +"\n" +
    "if문 : " + str(language_dictionary['if문']) + "\n" +
    "딕셔너리 : " + str(language_dictionary['딕셔너리']) + "\n" +
    "메서드 : " + str(language_dictionary['메서드']))

life_number = {'레오나르도 다빈치' : [67,77],
            '라파엘로' : [37,46],
            '미켈란젤로' :  [89, 98],
            '도나텔로' : [80, 86],
            '고흐' : [37,64]}
for person, number in life_number.items():
        print(person.title() + 'likes ' + str(number[0]) + ',' +str(number[1]))
