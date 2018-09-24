# 직원
"""
Employee 클래스를 만들자. The __init__() 메서드는 이름과 성, 연봉을 받고 이들을
각각 속성으로 저장해야 한다. 연봉을 기본값으로 5천 달러 올리지만, 증가분을 지정할
수도 있는 given_raise()메서드를 만들자.
"""

class Employee():
    """직원의 정보를 표시하는 클래스"""

    def __init__(self, first_name, last_name, salary):
        """이름과 성, 연봉의 속성을 저장한다."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def given_raise(self, amount=5000):
        """연봉의 값을 지정해준다"""
        self.salary += amount
