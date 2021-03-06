# 매개변수
def display_message():
    """함수를 배우면서 알게 된 내용을 표시한다"""
    print("함수에서 정의한 작업을 실행하고 싶을 때는 함수를 호출한다." +
        " 그 작업을 여러 번 실행해야 하더라도 같은 코드를 몇 번이고 다시 쓸" +
        " 필요는 없다. 그 작업 전용으로 만든 함수를 호출하기만 하면 파이선은" +
        " 함수 내부의 코드를 실행한다. 함수를 쓰면 프로그램을 쉽게 만들고, " +
        "읽고, 수정할 수 있다")

display_message()

def favorite_book(book_title):
    """'내가 좋아하는 책은 이상한 나라의 엘리스입니다'를 출력해야한다."""
    print("\n내가 좋아하는 책은 " + book_title.title() + "입니다.")

favorite_book('이상한 나라의 엘리스')
