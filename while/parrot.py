# input()함수가 동작하는 법
message = input("Tell me something and I will repeat it back to you: ")
print(message)
"""
input() 함수는 매개변수를 하나만 받는다 바로 사용자가 직접 입력하도록 기다리는
프롬프트가 잇는데 이 프롬프트에 입력한 값이 매개변수이다 이예제에서는 첫 번째 행을
실행 할 때 사용자에게 Tell me something and I will repeat it back to you: 라는
문구가 표시된다 프로그램은 사용자가 응답을 입력할 때까지 대기하고 사용자 입력을 받으
면 실행을 계속합니다 응답은 message 변수에 저장되며 print(message)로 사용자 입력을
출력한다
"""
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
"""
첫번째와 두번째 행에서 사용자에게 메시지를 입력하거나 종료 값('quit')을 입력하는
두 가지 옵션이 있음을 알리는 프롬프트를 정의했다. 사용자가 입력을 저장할
변수를 message로 만들었다 message는 빈 문자열 ""로 정의했으므로 파이썬이
처음 while 행에 도달햇을 때 체크할 것이 있다 프로그램을 처음 실행하고 파이썬이
while 문에 도달하면 message 값과 'quit'을 비교하짐나 아직 사용자는 아무것도
입력하지 않았다 파이썬이 비교할 대상이 없으면 프로그램을 계속 진핼할 수 없다
이 문제를 해결하기 위해 message 에 초깃값을 지정한 것이다 단순한 빈 문자열이지만
파이썬은 이 값을 인식하고 비교하므로 while 루프로 진입할수 있다 while 루프는
message의 값이 'quit' 이 아닌 한 계속 실행된다
"""
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
"""
위의 프로그램은 단어 'quit'을 실제 메시지처럼 출력한다는 것만 제외하면 잘 작동한다
이 문제는 if 테스트를 써서 수정할 수 있다
"""
# 플래그 사용하기
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
"""
여러 조건 중 맞지 않는 조건이 하나라도 있을 때 프로그램을 끝내야 한다면, 변수 하나를
정의해 전체 프로그램을 계속할지 끝낼지 판단하게 할 수 있다 이런 변수를 플래그 라
부르며 프로그램에 대한 신호처럼 동작한다 플래그가 True면 계속 실행되고, 플래그를
False로 바꾸는 이벤트가 일어나면 멈추도록 프로그램을 고쳐 쓸수 있다
"""
