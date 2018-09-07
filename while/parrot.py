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
