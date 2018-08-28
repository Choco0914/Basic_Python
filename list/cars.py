# 리스트 정리하기
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# sort()메서드는 리스트 순서를 영구적으로 알파벳 순서로 바꿔준다
cars.sort(reverse=True)
print(cars)
"""
sort() 메서드에 매개변수로 revers=True를 전달하면 리스트를 알파벳
반대 순서로 정렬할수 있다 역시 영구적으로 바뀐다
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
"""
sorted()함수는 리스트를 특정 순서로 표시하지만, 리스트 실제 순서는 바뀌지 않는다
sorted()함수에 revers=True 매개변수를 추가하면 알파벳 반대 순서로 표시할수 있다
"""
# 리스트를 반대 순서로 출력
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
"""
reverse()메서드를 사용하면 리스트의 순서를 반대로 바꾼다 알파벳 순서는
고려하지 않는다 리스트 목록은 계속 바뀐상태를 유지하고 reverse()메서드를 다시
이용하면 원상태로 돌아간다
"""
# 리스트 길이 구하기
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
"""
len() 함수로 리스트의 길이를 구할수 있다 항목이 네 개 이므로 네 개가 출력된다
파이썬은 리스트 항목의 개수를 셀 때 1부터 시작하므로 0에서 시작하는 에러가 생기지는
않는다
"""
