# 여러 파일 다루기
"""
분석할 책을 추가해보자. 하지만 먼저 이 프로그램의 상당 부분을 count_words()함수로
옮겨야한다. 그렇게 하면 여러 책을 분석하기가 한결 쉬워질 것이다.
"""
def count_words(filename):
    """파일에 있는 단어를 센다."""
    try:
        with open('text_files/' + filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 파일에 들어 있는 단어를 센다.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + "has about " + str(num_words) +
        " words.")

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
    'little_women.txt']
for filename in filenames:
    count_words(filename)
"""
try-except 블록은 중요한 장점을 두 가지 제공한다. 사용자에게 트레이스백이
노출되지 않게 막았고, 에러가 일어나도 텍스트 분석을 계속할 수 있다.
어떤 파일이 존재하지 않아 생긴 FileNotFoundError를 처리하지 않았다면 사용자에게
트레이스백 전체가 노출되었을 테고 프로그램은 없는 파일 분석을 시도하다가 멈췄을
것이다. 다른 파일은 분석하지 못하게 되버린다.
"""
# 조용히 실패하기
"""
이전 예제에서는 파일이 존재하지 않음을 사용자에게 알렸다.
하지만 사용자에게 모든 예외를 보고할 필요는 없다. 가끔은 프로그램이 마치 예외가
일어나지 않았던 것처럼 조용히 실패하길 원할 때도 있다. 프로그램이 조용히 실패하게
하려면 try 블록은 일반적으로 쓰고, except 블록에서 아무 일도 하지 않도록 파이썬에
명시적으로 지시한다. 파이썬에는 블록에서 아무 일도 하지 말라고 지시하는 pass문이
있다.
"""
def count_words(filename):
    """파일에 있는 단어를 센다."""
    try:
        with open('text_files/' + filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 파일에 들어 있는 단어를 센다.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + "has about " + str(num_words) +
        " words.")

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
    'little_women.txt']
for filename in filenames:
    count_words(filename)
"""
위의 코드를 실행하게 되면 except 블록의 코드가 실행되지만, 아무 일도 일어나지
않는다. 트레이스백도 출력되지 않고, 에러에 대해 설명하는 메세지도 없다.
사요앚는 존재하는 각 파일에 단어가 몇 개 있는지 알 수 있지만, 파일이 존재하지
않는다는 사실에 대해서는 알 수 없다.

pass 문은 플레이스홀더처럼 동작하기도 한다. 프로그램 실행 중 특정 지점에서 아무것도
하지 않기로 했으며, 나중에는 뭔가 하게 될 수도 있다는 메모이다. 예를 들어 이
프로그램에서는 존재하지 않는 파일 이름을 missing_files.txt 파일에 기록할 수 있다.
사요앚는 이 파일을 볼 수 없지만, 우리는 파일을 읽고 존재하지 않는 텍스트 파일에
대처할 수 있다.
"""
