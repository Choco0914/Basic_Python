# 클래스와 인스턴스 다루기
"""
클래스로 여러 가지 현실 상황을 나타낼수 있다. 일단 클래스를 만들면 그 뒤에는
그 클래스로 만든 인스턴스를 다루며 대부분의 시간을 보낸다. 가장 먼저 할 일은 특정
인스턴스와 연결된 속성을 수정하는 것이다. 인스턴스의 속성을 직접 수정할 수도 있고,
특별한 방법으로 속성을 업데이트하는 메서드를 만들 수도 있다.
"""
# Car class
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

my_new_car = Car('audi', 'a4', 2018)
print(my_new_car.get_descriptive_name())
"""
Car 클래스의 첫번째 메서드 에서는 Dog 클래스와 마찬가지로 __init__() 메서드를 정의
하면서 self 매개변수를 첫 번째로 썼다. 다른 매개변수 make와 model, year도
정의 했다. __init__() 메서드는 이드 매개변수를 받고 이 클래스에서 만들 인스턴스와
연결될 속성에 저장한다. Car에서 새 인스턴스를 만들 때는 제조사와 모델, 생산연도를
제공해야 한다.

두번째 메서드인 get_descriptive_name() 은 자동차의 year과 make, model 을 받아
자동차를 설명하는 읽기 쉬운 문자열로 바꿔준다. 이렇게 하면 각 속성값을 출력하는 번거
로움이 줄어든다. 이 메서드에서는 self.make, self,model, self,year 로 속성값에
접근했다. 마지막으로 Car 클래스에서 인스턴스를 새로 만들고 my_new_car 변수에
저장했다. 그리고 get_descriptive_name()을 호출해 어떤 자동차인지 출력했다.
"""
# 속성의 기본값 설정
"""
클래스의 모든 속성은 초깃값이 설령 0이거나 빈 문자열이라도 기본값이 필요하다.
기본값을 설정할 때는 그 값을 __init__() 메서드 안에 넣어두는 게 합리적이다.
속성에 기본 값을 정해 두면 그 속성에 해당하는 매개변수는 생략해도 된다.

자동차의 주행거리를 의미하는 odometer_reading 속성을 만들었다. 각 자동차의 주행
거리표시기(dodometer)를 읽기 쉽게 read_odomerter() 메서드도 추가했다. 그런데
차를 출고했을 때 주행거리는 0이므로 속성의 기본값으로 0으로 지정했다.
"""
my_new_car.read_odomerter()

# 속성값 바꾸기
"""
속성값을 바꾸는 방법은 세 가지이다. 인스턴스에서 값을 직접 바꿀수 있고, 메서드에서
값을 정할 수도 있고, 정해진 만큼만 늘리는 메서드를 만들 수도 있다.
"""
# 속성값 직접 바꾸기
my_new_car.odometer_reading = 23 # 1행
my_new_car.read_odomerter()
"""
1행에서는 점 표기법을 사용해 자동차의 odometer_reading 속성에 접근하고 그 값을
직접 바꿨다. 이 행은 파이썬이 my_new_car 인스턴스를 읽고 연결된 odometer_reading
속성을 찾아 그 값을 23으로 바꾸게 한다.
"""
# 메서드를 통해 속성값 바꾸기
"""
속성값을 바꾸는 메서드가 있다면 편리하다. 속성에 직접 접근하지 않고 메서드에 새 값을
넘겨 내부적으로 수정할 수 있다.
"""
my_new_car.update_odometer(23)
my_new_car.read_odomerter()
"""
Car에서 수정한 내용은 update_odometer()를 추가한 것 뿐이다. 이 메서드는 주행거리
값을 받고 그 값을 self.odometer_reading에 저장한다. update_odometer()를 호출하고
23을 배개변수로(메서드 정의의 mileage 매개변수에 대응) 넘겼따. 이 메서드는 표시기의
값을 23으로 바꾸며 read_odomerter()에서 그 주행 거리를 출력한다.
"""
# 주행거리 표시기를 롤백할 수 없게 만드는 코드 추가
"""
update_odometer() 속성을 수정하기 전에 새 값이 합리적인지 확인한다.
새 주행거리인 mileage가 기존 주행거리 self.odometer_reading보다 크거나 같다면
주행거리를 업데이트 한다. 새 주행거리가 기존 주행거리보다 작다면 주행거리 표시기를
롤백할 수 없다는 경고를 표시한다.
"""

# 메서드를 통해 속성값을 정해진 만큼씩만 바꾸기
"""
때로는 속성값을 완전히 새로운 값으로 지정하기보다는 일정한 양만큼만 바꿔야
할 때도 있다. 중고 자동차를 샀다면 구입 서점과 등록 시점 사이에 100마일을 추가한다고
하자.
"""
print("\n")

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odomerter()

my_used_car.increment_odometer(100)
my_used_car.read_odomerter()
"""
increment_odometer() 메서드는 주행거리를 숫자로 받고 그 값을 self.odometer_reading
에 더한다. 그리고 중고차 my_used_car를 만들었다. 그리고 나서
update_odometer()를 호출하면서 23500을 넘겨 주행거리 표시기를 23500으로 지정했다.
다음으로 increment_odometer()를 호출해서 100을 넘겨 자동차를 구입한 후
등록할 때까지 주행한 100마일을 더했다.
"""
