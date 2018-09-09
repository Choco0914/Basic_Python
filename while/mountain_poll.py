# 사용자가 입력한 갑으로 딕셔너리 채우기
responses = {}
# 설문이 활성화됐다는 플래그를 설정했다
polling_active = True

while polling_active:
    # 이름과 응답을 묻는다.
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday? ")
    # 응답을 딕셔너리에 저장한다
    responses[name] = response
    # 다른 사람도 설문에 참여할지 묻는다
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# 설문이 끝났다. 결과를 출력한다.
print("\n---Poll Results ===")
for name, response in responses.items():
    print(name + "would lke to climb " + response + ".")
print(responses)
"""
while 루프 안에서 필요한 만큼 입력을 받을 수 있다. 루프가 반복될 때마다 참가지 이름
과 응담을 묻는 설문 프로그램을 만들어보자. 각 응답을 특정 사용자가 연결해야 하므로
수집한 데이터는 딕셔너리에 저장한다.
위 프로그램은 먼저 빈 딕셔너리 ersponses와 설문이 활성화됐다는 플래그
polling_active를 정의한다. polling_active가 True인 한 파이썬은 while 루프의
코드를 계속 실행한다. 루프 안에서 사용자는 사용자 이름과 올라가보고 싶은 산을
묻는 프롬프트를 받는다 이 정보를 responses 딕셔너리에 저장하고, 설문을 계속하지
묻는다. yes를 입력하면 프로그램은 while 루프에 다시 진입한다. no를 입력하면
polling_active 플래그가 False로 바뀌고 while 루프를 빠져나와 설문 결과를
표시하는 마지막 코드 블록이 실행된다.
"""
