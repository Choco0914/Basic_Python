# 리스트 전달
def greet_users(names):
    """리스트의 각 사용자에게 단순한 환영 인사를 출력한다."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

username = ['hannah', 'ty', 'margot']
greet_users(username)
