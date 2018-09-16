"""레스토랑을 나타나낼때 쓸수 있는 class"""
class Restaurant():
    """Restaurant를 모델화"""
    def __init__(self, restaurant_name, cuisine_type):
        """restaurant_name과 cuisine_type 속성을 초기화"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """restaurant_name과 cuisine_type정보를 출력한다."""
        print("Restaurant name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        """레스토랑이 열렸다는 메시지를 출력한다."""
        print(self.restaurant_name.title() + "was opened")
