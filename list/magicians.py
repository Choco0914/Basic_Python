# 전체 리스트에 대해 루프 실행하기
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
"""
for문을 이용해 magicians 리스트안의 항목들을 magician 변수에 저장하고
print()메서드를 이용해 출력한다 첫번째 항목을 저장하고 출력후 for문으로 돌아가
두번째 항목을 magician변수(변수 이름은 아무거나 사용 가능하다)에 저장하고
다시 출력하고  다시 세번째 항목을 magician 변수에 저장후 출력하는 과정을 반복한다
"""
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
"""
for 루프 안에서는 원하는 만큼의 여러 행의 코드를 쓸 수 있다
for magician in magicians 다음에 있는 들여 쓴 행은 모두 루프 안이라 간주되며,
들여 쓴 각 행은 리스트의 각 값에 대해 한 번씩 실행된다 따라서 리스트의 각 값을
원한는 만큼 조작할수 있다 for  루프로부터 루프의 마지막 행까지를 루프 블록이라고 한다
"""
print("Thank you, everyone. That was a great magic show!")
