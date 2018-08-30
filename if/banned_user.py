# 값이 리스트에 있는지 체크하기
"""
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
특정 값이 리스트에 이미 존재하는지 체크할 때는 키워드 in을 사용한다
피자 전문점에 사용할 코드를 만든다 하면 고객에 요청한 토핑 리스트를 만들고,
토핑이 리스트에 존재하는지 체크할것이다
"""
# 값이 리스트에 없는지 체크하기
banned_users = ['andrew', 'carolina', 'david']
user = 'marrie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
"""
값이 리스트에 없는지 체크해야 할 때도 있다 이럴때는 키워드 not을 쓸수있다
예를들어 포럼에 댓글을 달 수 없도록 차단된 사용자 리스트가 있다고 하면 사용자가
댓글을 전송하기 전에 차단됐는지 체크할 수 있다
"""
# 불리언 표현식
"""
프로그래밍에 더 익숙해지면 어떤 시점에서는 불리언 표현식이라는 용어를 듣게된다
불리언 표현식은 조건 테스트의 다른 이름일 뿐이다 불리언 값은 조건 표현식을 평가한
다음의 값과 마찬가지로 True 또는 False다
예를 들어 게임이 실행중인지, 사용자가 웹사이트 특정 콘텐츠를 편집할 수 있는지
같은 조건을 저장할 때 자주 사용한다
ex) game_active = True
ex2) can_edit = False
""
