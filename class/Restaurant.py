# This is Restaurant
"""
Restaurant 클래스를 만들자. Restaurant의 __init__() 메서드는 restaurant_name과
cuisine_type 두 가지 속성을 저장해야 한다. 이들 정보를 출력하는
describe_restaurant() 메서드와 레스토랑이 열렸다는 메시지를 출력하는
open_restaurant() 메서드를 만들어보자.
"""
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

restaurant = Restaurant('nice restaurant', 'cold noodles')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

another_restaurant = Restaurant('beautiful restaurant', 'bread')
another1_restaurant = Restaurant('awsome restaurant', 'stake')
another2_restaurnat = Restaurant('cool restaurant', 'icecream')
another_restaurant.describe_restaurant()
another1_restaurant.describe_restaurant()
another2_restaurnat.describe_restaurant()
