# 중첩
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
"""
이따금 딕셔너리를 리스트에 저장하거나 리스트를 딕셔너리 값으로 저장해야 할 때가 있다
이걸 중첩(nesting)이라 한다 딕셔너리를 리스트에, 리스트를 딕셔너리에, 심지어
딕셔너리를 다른 딕셔너리에 저장할 수 있다
"""

# 외계인을 자동으로 생성하는 코드를 만들자
aliens= []

for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))
"""
range()가 숫자 리스트 를 반환한다 이 리스트는 파이썬이 루프를 몇 번 반복할지 정하는
역할만 한다 루프의 각 단계마다 new_alien에서 새 외계인을 만들고, aliens.append()
에서 각 새 외계인을 aliens 리스트에 추가했다 그리고 슬라이스를 써서 처음 5명의
외계인을 출력했고, 마지막으로 리스트 길이를 출력해서 외계인 30명으로 구성된
함대를 완성한걸 확인했다
"""
aliens= []

for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['spped'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("...")
"""
처음 3명의 외계인만 수정하기로 했으니 처음 3명의 외계인만 포함한 슬라이스를 만들어 루
프를 실행한다 지금은 모든 외계인이 녹색이지만, 항상 그렇다고 보장할 수는 없으므로
if 문을 써서 녹색 외계인만 수정한다. 외계인이 녹색이면 색을 'yellow'로,
속도를 'medium'으로, 점수를 10점으로 바꾼다
"""
aliens= []

for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['spped'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")
"""
위 루프를 elif 블록으로 확장해 노란색 외계인을 빨갛고, 빠르게 움직이는 15점짜리
외계인으로 바꿀수 있따 전체 프로그램을 쓰지는 않고 루프만 다시 쓰면 위와같은 모양이
된다
"""
