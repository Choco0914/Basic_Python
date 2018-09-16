"""전기자동차를 나타낼 때 쓸 수 있는 코드"""

from car_s import Car

class Battery():
    """전기자동차의 배터리를 모델화하려는 단순한 시도"""

    def __init__(self, battery_size=70):
        """배터리의 속성 초기화"""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리 크기를 설명하는 문장 출력"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """이 배터리가 제공하는 주행 가능 거리를 출력한다."""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full change."
        print(message)


class ElectricCar(Car):
    """전기자동차에만 해당하는 특징을 나타낸다"""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화한다."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """전기자동차에는 연료 탱크가 업습니다."""
        print("This car doesn't need a gas tank!")
