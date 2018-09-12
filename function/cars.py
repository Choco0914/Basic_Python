"""
딕셔너리에 자동차 정보를 저장하는 함수를 만들자. 이 함수는 항상 제조사 이름과
모델명을 받아야 한다. 그리고 키워드 매개변수를 임의의 숫자만큼 받아야 한다.
필수 정보와 색을 넣고 옵션과 기능 같은 두 가지 키-값 쌍을 추가해 함수를 호출해라
이 함수는 다음과 같이 호출해야 한다.
car = make_car('subaru', 'outback', color='blue', tow_package=True)
"""
def make_car(name, nick_name, **cars_info):
    """자동차 정보를 저장하는 함수"""
    car = {}
    car['name'] = name
    car['nick name'] = nick_name
    for key, value in cars_info.items():
        car[key] = value
    return(car)

japna_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(japna_car)
