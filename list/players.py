#리스트 자르기
players = ['charles', 'martina', 'micael', 'florence', 'eli']
print(players[0:3])
"""
슬라이스를 만들때는 두개의 인덱스가 필요하다 첫 번째 인덱스는 시작하는 항목의 인덱스
두 번째 인덱스는 끝나는 항목이 아니다 range()함수와 마찬가지로 파이썬은 두 번째
인수 바로 앞의 항목에서 멈춘다 리스트의 처음 세 항목을 꺼낸다면 인덱스 0, 1, 2를
요청하게 된다
"""
print(players[1:4])
# 어디서 자르고 싶은지 첫번째 인덱스에서 정하고 어디까지 꺼내서 쓸건지 두번째 인덱스
# 에서 정한다 두번째 인덱스 바로앞 항목에서 멈춘다는것을 명심하자
print(players[:4])
# 첫번째 인수가 비어있으면 자동으로 리스트의 처음에서 시작해 슬라이스 하게 된다
print(players[2:])
# 마찬가지로 시작할 부분을 정하고 마지막을 정하지 않으면 리스트의 끝까지 슬라이스
# 하게 된다
print(players[-3:])
# -를 사용하면 마지막 항목부터 리스트가 시작된다 마지막 3명을 출력해보자
# 슬라이스에 루프 실행하기
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
# 슬라이스를 루프를 이용해 출력해보았다
