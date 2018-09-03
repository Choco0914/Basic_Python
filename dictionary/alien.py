#Basic dictionary
alien_0 = {'color' : 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
"""
alien_0 딕셔너리는 외계인 색과 점수를 저장한다 두 print문은 정보에 접근하고
print(alien_0['color']) 는 green을 출력하게 되고, print(alien_0['points'])는
5를 출력하게 된다 dictionary는 처음 배울 때는 익숙치 않으니 연습이 필요하다
"""
# use dictionary
"""
파이썬 딕셔너리는 키-값 쌍의 모음이다 각 키는 값에 연결되며, 키에 연결된 값에
접근할 때도 키를 사용한다. 키의 값은 숫자, 문자열, 리스트, 심지어
다른 딕셔셔너리도 가능하다
"""
# contact dictionary value
alien_0 = {'color' : 'green'}
print(alien_0['color'])
# 딕셔너리에 쓸 수 있는 키-값 쌍의 숫자에는 제한이 없다
alien_0 = {'color' : 'green', 'points': 5}

new_points = alien_0['points']
print("You just earned " +str(new_points) + " points!")
"""
new_points는 딕셔너리에서 키'points'의 값을 가져온다 그리고
그 값을 new_points 변수에 저장한다 str()은 정수 값을 문자열로 바꿔서 플레이어가
몇 점을 얻었는지 출력한다
"""
# 새 키-값 쌍 추가하기
print('\n' + str(alien_0))

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
"""
딕셔너리는 문자열이 아니라 str을 통해 문자열로 바꿔줬다
그리고 마지막 버전에서 키-값 쌍이 네 개 생겼다 원래 두 땃응ㄴ 색과 점수르 저장하고
추가한 두 쌍은 외계인 위치를 저장했다. 키-값이 표시되는 순서는 추가한 순서와
일치하지 않는다 파이썬은 각 키-값 쌍을 저장한 순서는 신경 쓰지 않고 각 키와 값의 연결
만 중시한다
"""
# start empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print("\n" + str(alien_0))
"""
때로는 빈 딕셔너리로 시작하고 새 항목을 추가하는 방법이 더 간편하거나 필요할 때도
있다 빈 딕셔너리로 시작하려면 빈 중괄호로 딕셔너리를 정의하고 다른 행에서 키-값 쌍을
추가한다
"""
# modify value of dictionary
alien_0 = {'color' : 'green'}
print("\nThe alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + ".")
"""
딕셔너리의 값을 수정할 때는 딕셔너리 이름 다음에 대괄호 속에 키를 쓰고 그 키에 연결할
새 값을 지정한다.
"""
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium',}
print("Original x-position: " + str(alien_0['x_position']))

# 외계인을 오른쪽으로 움직인다
# 현재 속도를 기준으로 외계인이 얼마나 빨리 움직이는지 판단한다

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 이 외계인을 빠른놈이다
    x_increment = 3

# 새 위치는 이전 위치에 증가분을 더한 값이다
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
"""
먼저 외계인의 첫 x 위치와 y 위치, 'medium' 속도를 지정했다 단순하게 보이려고 색과
점수는 생략했지만, 색과 점수가 있더라도 똑같이 작동한다 외계인이 오른쪽으로 얼마나
빨리 움직이는 보기 위해 x_position의 원래 값도 출력했다
if-elif-else 문을 써서 외계인이 오른쪽으로 얼마나 빨리 움직이는지 판단하고
그 값을 x_increment 변수에 저장했다 외계인의 속도가 'slow'이면 한 칸을, 속도가
'medium'이면 두 칸을, 'fast'이면 세 칸을 오른쪽으로 움직인다. 이동거리를
x_position 값에 더하고 그 결과를 딕셔너리의 x_position에 저장했다 이 외계인은
중간 속도이므로 오른쪽으로 두 칸 이동했다
만약 중간 속도 외게인을 빠른 속도로 바꾸고싶다면 if문 위에 alien_0['speed'] = 'fast'
코드를 추가하면 x_increment에 더 큰 값을 할당한다
"""
# 키-값 쌍 제거하기
alien_0 = {'color' : 'green','points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
"""
딕셔너리에 저장된 정보가 더 이상 필요 없다면 del 문을 써서 완벽히 제거할 수 있다
del 문에는 디겻너리 이름과 제거할 키만 필요하다
"""
