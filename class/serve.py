"""
기본값이 0인 number_served 속성(서빙한 고객 숫자)을 추가하자.
이 클래스에서 retaurant 인스턴스를 만들자. 레스토랑에서 서빙한 고객 숫자를 출력
하고, 이 값을 바꿔서 다시 출력하자.
"""
class Restaurant():
    """Restaurant를 모델화"""
    def __init__(self, restaurant_name, cuisine_type):
        """
        restaurant_name과 cuisine_type, number_served 속성을 초기화
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """restaurant_name과 cuisine_type정보를 출력한다."""
        print("Restaurant name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        """레스토랑이 열렸다는 메시지를 출력한다."""
        print(self.restaurant_name.title() + "was opened")

    def serve_client(self):
        """서빙한 고객 수를 출력한다."""
        print("Number of customers served: " + str(self.number_served))

    def set_number_served(self, serbed):
        """서빙한 고객 숫자를 지정한다."""
        self.number_served = serbed

    def increment_number_served(self, increment):
        """서빙한 고객 숫자를 늘린다."""
        self.number_served += increment
"""
레스토랑에서 서빙한 고객 숫자를 출력하고, 이 값을 바꿔서 다시 출력해라.
"""
client = Restaurant('nice restaurant', 'cold noodles')
client.serve_client()
client.number_served = 12
client.serve_client()
"""
서빙한 고객 숫자를 저장하는 set_number_served() 메서드를 추가해라 새 숫자로
이 메서드를 호출하고 값을 다시 출력해라
"""
client.set_number_served(17)
client.serve_client()
"""
서빙한 고객 숫자를 늘리는 increment_number_served() 메서드를 추가하자
원하는 숫자, 예를들어 영업일 하루 동안 서빙한 숫자로 이 메서드를 호출해라.
"""
client.increment_number_served(39)
client.serve_client()
