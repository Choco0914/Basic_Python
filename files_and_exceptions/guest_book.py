# 방명록
"""
사용자에게 이름을 묻는 while 루프를 만들자. 사용자가 이름을 입력하면 화면에 환영
인사를 출력하고 그들이 방문했다는 내용을 guest_book.txt 파일에 한 행 기록하자.
이름마다 한 행씩 차지하는지 확인해라.
"""

filename = 'guest_book.txt'

guests = []
guests_exit = True
guest_question = "\nWhat is your name? "
guest_question += "\n(Enter 'quit' when you are finished.)\n"
while guests_exit:
    guest = input(guest_question)
    if guest == 'quit':
        guests_exit = False
    else:
        guests.append(guest)
        
with open(filename, 'w') as file_object:
    for guest in guests:
        file_object.write(guest + "\n")
