"""유저와 관리자 클래스를 정리했다."""

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

class Privileges():
    """특권을 저장하고 출력한다."""
    def __init__(self):
        """특권의 속성을 초기화한다."""
        self.privilege = []

    def privileges(self, pri):
        self.privilege.append(pri)

    def show_privileges(self):
        print("\nHere is administer's privileges ")
        for admin_privilege in self.privilege:
            print("- " + admin_privilege.title())

class Admin(User):
    """사용자를 관리하는 관리자"""
    def __init__(self, first_name, last_name):
        """사용자를 속성을 초기화한다."""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
