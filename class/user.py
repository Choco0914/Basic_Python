# User
"""
User 클래스를 만들자. first_name과 last_name 속성을 만들고 일반적으로 사용자
프로필에 저장할 만한 여러 가지 다른 속성을 추가하자. 사용자 정보를 요약해
출력하는 describe_user() 메서드를 만들어라 사용자에게 환영 인사를 보내는
greet_user() 메서드를 만들자.
"""

class User():
    """User 정보를 요약하고 환영하는 메시지를 만든다"""
    def __init__(self, first_name, last_name):
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

dave = User('dave', 'lie')
robin = User('robin', 'winchester')
luke = User('luke', 'ronaldo')

dave.describe_user()
dave.greet_user()
robin.describe_user()
robin.greet_user()
luke.describe_user()
luke.greet_user()
