# 덧셈
"""
사용자에게 숫자 입력을 요청할 때 항상 있는 문제는 사용자가 숫자가 아닌 텍스트를
입력하는 문제이다. 입력 내용을 정수로 바꾸려 하면 TypeError가 일어날 거다.
숫자 두 개를 요청하는 프로그램을 만들자. 두 숫자를 더하고 결과를 출력해보자.
입력 중 하나가 숫자가 아닐 때 일어난 TypeError를 잡아, 알기 쉬운 에러 메세지를
출력해라. 숫자 두 개를 입력해보고, 숫자 대신 텍스트를 입력해서 프로그램을 테스트하자.
"""
print("Give me the your number")
print("Enter the 'q' to quit")

while True:
    try:
        first_number = input("\nFirst Numbers here: ")
        if first_number  == 'q':
            break
        first_number = int(first_number)
        second_number = input("\nSecond Numbers here: ")
        if second_number == 'q':
            break
        second_number = int(second_number)
    except ValueError:
        print("Please enter only init!")
    else:
        result = first_number + second_number
        print("The sum of the two numbers is " + str(result))
