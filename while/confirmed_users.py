# 항목을 리스트에서 다른 리스트로 옮기기
unconfirmed_users = ['alice', 'brain', 'Candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
"""
처음에 확인되지 않은 사용자 리스트(Alice, Brian, Candace)와 확인된 사용자를
담을 빈 리스트로 시작한다. while 루프는 unconfirmed_users 리스트가 비어 있지
않은 한 계속 실행된다. 이 루프 안에서 pop()함수는 unconfirmed_users의 마지막
에서부터 확인되지 않은 사용자를 한 번에 하나씩 제거한다. Candace는 unconfirmed_users
리스트의 마지막에 있으므로 그녀의 이름이 첫 번째로 제거되고, current_user에
저장됐다가 confirmed_users 리스트에 추가된다 다음은 Brian이고, 그다음은 Alice다
각 사용자에서 확인 메세지를 출력하고 확인된 사용자 리스트로 옮기는 것으로 사용자
확인을 흉내 내었다. 확인되지 않은 사용자 리스트가 줄어들면서 확인된 사용자 리스트는
커진다
"""
