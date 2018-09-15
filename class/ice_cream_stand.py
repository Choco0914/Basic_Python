# 아이스크림 가판대
"""
아이스크림 가판대도 일종의 음식점이다. 예전에 만든 Restaurant 클래스를 상속하는
IceCreamStand 클래스를 만들자. 어느 쪽이든 상관없으니 더 마음에 드는 클래스를
택하자. 아이스크림 맛 리스트를 저장하는 flavors 속성을 추가하자. 이들 맛을 표시하
는 메서드를 만들자. IceCreamStand 인스턴스를 만들고 이 메서드를 호출해라.
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

class IceCreamStand(Restaurant):
    """아이스크림을 판매하는 가판대"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add(self, icecream):
        """아이스크림 종류를 저장한다."""
        self.flavors.append(icecream)

    def taste(self):
        """아이스크림 맛을 출력한다."""
        print("\nIce cream types: ")
        for flavor in self.flavors:
            print("\t- " + flavor.title())

icecream = IceCreamStand('super', 'ice cream')
icecream.add('choco')
icecream.add('vanila')
icecream.add('coffee')
icecream.taste()
