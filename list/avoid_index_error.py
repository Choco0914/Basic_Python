# 인덱스 에러 피하기
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
위와같은 예제는 다음과 같은 에러를 보여준다
Traceback (most recent call last):
  File "avoid_index_error.py", line 3, in <module>
    print(motorcycles[3])
IndexError: list index out of range
파이썬은 인덱스3에 있는 항목을 반환하려 합니다 하지만 motorcycles 리스트에는
인덱스 3인 항목이 없다 리스트 인덱스는 하나씩 줄어들기 때문에 이 에러는 자주 일어나는
에러이다 사람들은 1부터 세니가 세 번째 항목의 인덱스가 3이라 생각하지만, 파이썬은
0부터 세니까 세 번째 항목의 인덱스는 2이다
"""
