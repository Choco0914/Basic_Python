dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
"""
리스트가 아닌 튜플을 생성하였다 튜플은 리스트와 달리 []대괄호가 아닌 ()소괄호를
사용한다 그리고 불변적(immutable)이라 하며 바뀌지 않는 리스트 를 튜플이라한다
dimensions[0] = 250
Traceback (most recent call last):
  File "dimensions.py", line 8, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
튜플의 항목을 수정하려 하면 위와같은 에러가 발생한다
"""
for dimension in dimensions:
    print(dimension)
# tuple도 리스트와 마찬가지로 for loop문을 이용할수 있다
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
# tuple은 수정할수 없지만 새값을 할당하는건 가능하다 즉, tuple을 새로 정의하면
# tuple의 내용을 바꿀수있다
# 만약 프로그램 전체에 걸쳐 바뀌면 안 되는 값이 있다면 튜플을 저정해서 이용하자
