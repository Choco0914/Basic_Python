#숫자 리스트 만들기
for value in range(1, 5):
    print(value)
# range()함수는 숫자 1부터 4까지마 ㄴ출력한다 range(시작_숫자, 끝_숫자)에서
# 끝_숫자는 포함되지 않는다 range() 함수는 시작_숫자에서 끝_숫자에 도달하면 멈춘다
for value in range(1, 6):
    print(value)
numbers = list(range(1,6))
print(numbers)
# range()함수로 리스트를 만들었다 list함수안에 range()포함시키고 범위를 지정해주면
# 쉽게 1~5까지의 리스트를 만들수있다
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# 여기서 range()함수는 값 2에서 시작해 그값에 2를 더한다 마지막 값인 11에 도달하거나
# 지날 때까지 반복하므로 결과는 [2, 4, 6, 8, 10]을 만든다
# range(시작_숫자, 끝_숫자, 증가치)라 생각하면 된다
squares = [] # ...1
for value in range(1,11): # ...2
    square = value**2 # ...3
    squares.append(square) # ...4

print(squares) # ...5
"""
1부터 10까지의 제곱수(squares)리스트를 만든다하면 파이썬에서는
애스터리스크 두개(**)가 지수를 나타낸다
1에서는 빈 리스트 squares를 만들고 2에서는 range()함수를 이용해 1부터 10까지 루프를
실행했다 루프 안에서는 현재 값의 제곱을 만들어 그 값을 square 변수에 저장했따
4에서는 square의 새 값을 squares 리스트에 추가했다 마지막으로 루프가 실행을 마친뒤
제곱수 리스트를 5에서 출력했다
"""
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
# 위의 코드는 더 간결하게 바꾼 코드이다 코드를 간결하게 만드는데 주력하자!
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
# 파이썬 함수 일부는 숫자 리스트에만 사용할수 있다. 예를 들어 숫자 리스트에서
# 최댓갑이나 최솟값, 합계를 구하는 함수가 있다 위와 같은 경우이다
