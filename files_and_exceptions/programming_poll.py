# 프로그래밍 투표
"""
사람들에게 왜 프로그래밍을 좋아하는 묻는 while 루프를 만들자.
누군가 이유를 입력할 때마다 모든 응답을 저장한 파일에 그 이유를 추가하자.
"""
filename = 'programming_poll.txt'

programers = {}
how_exit = True
name = "What is your name?\n"
name += "(Enter 'quit' when you want to quit)\n"
programming = "Why do you like programming?\n"
while how_exit:
    question = input(name)
    if question == 'quit':
        how_exit = False
    else:
        question_2 = input(programming)
        programers[question] = question_2

with open(filename, 'w') as f:
    for name, programming in programers.items():
        f.write(name.title() +
        " likes programming for the following reasons: \n" + programming +
        "\n")
