"""
random 모듈에는 다양한 방법으로 난수를 생성하는 함수가 들어 있다.
randint() 함수는 지정한 범위안에서 정수를 반환한다.
"""
from random import randint

class Die():
    """주사위를 나타내는 클래스"""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        """1부터 주사위면 숫자 사이의 무작위 숫자를 출력한다."""
        return randint(1, self.sides)

dice = Die()

results = []
for roll_num in range(10):
    result = dice.roll_die()
    results.append(result)
print("\n10 rolls of a 6-sides die:")
print(results)

dice10 = Die(10)

results = []
for roll_num in range(10):
    result = dice10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sides die:")
print(results)

dice20 = Die(20)

results = []
for roll_numb in range(10):
    result = dice20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sides die:")
print(results)
