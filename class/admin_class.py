"""관리자 클래스만 정의했다."""
from users import User

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
