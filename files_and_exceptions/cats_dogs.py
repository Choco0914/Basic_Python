# 고양이와 개
"""
cats.txt, dogs.txt 두 파일을 만들자. 첫 번째 파일에는 고양이 이름을 최소한 세 개,
두 번째 파일에는 개 이름은 최소한 세 개 저장하자. 이 파일들을 읽고 파일 내용을
화면에 출력하는 프로그램을 만들자. 코드를 try-except 블록으로 감싸 FileNotFound
에러를 잡고, 파일이 존재하지 않을 때는 알기 쉬운 메시지를 출력하자.
파일 중 하나를 다른 위치로 옮기고 except 블록의 코드가 제대로 실행되는지 확인하자.
"""
def cats_dogs(filename):
    """동물들 이름을 출력한다."""
    try:
        with open('text_files/' + filename) as f_obj:
            names = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #파일에 있는 이름을 출력한다.
        print("There is " + filename + "animalsj's names:")
        print(names)

filename = 'cats.txt'
cats_dogs(filename)

filename = 'dogs.txt'
cats_dogs(filename)
