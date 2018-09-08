# While 루프 사용하기
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
"""
첫 번째 행에서 current_number의 값을 1로 설정해 1부터 시작했다
while루프는 current_number의 값이 5보다 작거나 같다면 계속 실행되게 만들었따
루프 안의 코드는 current_number의 값을 출력하고 current_number += 1로 값에
1을 더한다(+=연산자는 current_number = current_number + 1의 단축 표기이다)
파이썬의 조건 current_number <= 5를 만족하는 동안 루프를 계속 반복한다.
1은 5보다 작으므로 파이썬은 1을 출력하고 1을 더해 현재 숫자를 2로 만든다
2는 5보다 작으므로 파이썬은 2를 출력하고 1을 더해 현재 숫자를 3으로 만들며 이 과정을
반복한다 일단 current_number의 값이 5를 초과하면 루프가 멈추고 프로그램이 종료된다
"""
# 루프에서 continue 문 사용하기
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
"""
continue 문을 쓰면 조건 테스트 결과에 따라 루프 처음으로 돌아갈 수 있다
먼저 시작 값인 current_number를 0으로 설정했다. 이 값은 10보다 작으므로 while
루프에 진입한다. 일단 루프에 들어오면 1을 더하므로 current_number는 1이된다.
그리고 if 문에서 current_number를 2로 나눈 나머지를 검사한다. 나머지가 0이면,
즉 current_number가 2로 나뉠 수 있는 숫자이면 continue 문은 파이썬이 루프의
나머지 코드를 무시하고 처음으로 돌아가게 한다. 현재 숫자를 2로 나눌 수 없으면
루프의 나머지 코드가 실행되어 현재 숫자를 출력한다
"""
# 무한 루프 피하기!
x = 1
while x <= 5:
    print(x)
    x += 1
"""
위의 코드에서 실수로 x += 1행을 빼먹으면 이 루프는 영원히 실행된다.
무한 루프를 피하려면 모든 while 루프를 테스트해서 예상대로 멈추는지 확인하는 것이
좋다. 사용자가 특정 값을 입력햇을 때 프로그램이 멈추길 원한다면 프로그램을 실행하고
그 값을 입력해보자. 프로그램이 멈추지 않으면 프로그램에서 루프의 종료 조건인 값을
어떻게 처리하는지 훑어보자. 최소한 프로그램의 한 부분에서는 루프 조건을 False로
만들거나 break 문을 호출해야 한다
"""
