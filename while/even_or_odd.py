number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)

if number & 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + "is odd.")
"""
짝수는 항상 2로 나눌 수 있다. 그러므로 어떤 숫자를 2로 나눈 나머지가 0이라면(여기서
는 if number % 2 == 0)그 숫자는 짝수이다 그렇지 않으면 홀수
"""
