# 딕셔너리 안에 딕셔너리 담기
users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princetion',
    },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
"""
먼저 사용자 이름인 'aeinstein'과 'mucrie' 를 키로 써소 users 딕셔너리를 정의했다
각 키에 연결된 값은 각 사용자의 성과 이름, 위치를 포함한 딕셔너리이다
users 딕셔너리에 루프를 실행한다 파이썬은 각 키를 username 변수에 저장하고
각 사용자 이름에 연결된 딕셔너리는 user_info 변수에 저장한다 바깥족 딕셔너리의
루프 안 에서 사용자 이름을 출력한다
내부 딕셔너리에 접근해 사용자 정보를 저장한 user_info 딕셔너리에 있는 'first'와
'last', 'location' 세 가지 키가 있다 각 키를 써서 완전한 이름과 위치를 만들고,
사용자 정보를 요약해 출력한다 
"""
