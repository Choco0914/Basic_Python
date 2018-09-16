"""유저 클래스를 정의했다."""

class User():
    """User 정보를 요약하고 환영하는 메시지를 만든다"""
    def __init__(self, first_name, last_name,):
        """first_name과 last_name 속성을 초기화한다."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """사용자 정보를 요약해 출력한다"""
        print("\nThis user name is:")
        print(self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        """사용자에게 환영 인사를 보낸다."""
        print("\nHello " + self.first_name.title() +
        " " + self.last_name.title())
