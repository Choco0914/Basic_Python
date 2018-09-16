# Car class
"""자동차를 표현할때 쓸수 있는 클래스"""
class Car():
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make =make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 속성의 기본값 설정

    def get_descriptive_name(self):
        """알아보기 쉬운 이름 반환"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odomerter(self):
        """주행 거리를 나타내는 문장을 출력한다"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage): # 메서드를 통해 속성값 바꾸기
        """
        주행거리 표시기를 주어진 값으로 바꾼다.
        주행거리 표시기를 더 작은 값으로 바꾸려 하면 거부한다.
        """
        if mileage >= self.odometer_reading: # 주행거리 표시기를 롤백할
            self.odometer_reading = mileage # 수 없게 하기
        else:
            print("You can't roll bakc an odometer!")

    def increment_odometer(self, miles): # 메서드를 통해 속성값을
        """주행거래를 주어진 양만큼 늘린다.""" #정해진 만큼씩만 바꾸기
        self.odometer_reading += miles

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
