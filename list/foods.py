# 리스트 복사하기
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# 새로운 리스트인 friend_foods에 my_foods를 복사했다
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite food are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# append메소드를 이용해 my_foods와 friend_foods에 각각 음식을 한개씩 추가했다
# 출력하면 my_foods에는 cannoli가 추가되고 friend_foods에는 ice cream이 추가되었다
# 슬라이없이 한번 실행해보자
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite food are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
