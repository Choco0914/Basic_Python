# 로그인 시도
"""
연습문제 User 클래스에 login_attempts 속성(로그인 시도 횟수)을 추가하자.
login_attempts 값을 1씩 늘리는 increment_login_attempts() 메서드를 만들자.
login_attempts 값을 0으로 리셋하는 reset_loginattempts() 메서드도 만들자.
"""
class User():
    """User 정보를 요약하고 환영하는 메시지를 만든다"""
    def __init__(self, first_name, last_name):
        """first_name과 last_name 속성을 초기화한다."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """사용자 정보를 요약해 출력한다"""
        print("\nThis user name is:")
        print(self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        """사용자에게 환영 인사를 보낸다."""
        print("\nHello " + self.first_name.title() +
        " " + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1
        return(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        return(self.login_attempts)
"""
User 클래의 인스턴스를 만들고 increment_login_attempts()를 여러 번 호출하자.
login_attempts를 출력해서 값이 제대로 늘어났는지 확인하고 reset_login_attempts()
를 호출하자. login_attempts를 다시 출력해 0으로 리셋됐는지 확인하자
"""
login = User('cho', 'co')
print(login.login_attempts)
login.increment_login_attempts()
login.increment_login_attempts()
login.increment_login_attempts()
login.increment_login_attempts()
print(login.login_attempts)
login.increment_login_attempts()
print(login.login_attempts)
login.reset_login_attempts()
print(login.login_attempts)
