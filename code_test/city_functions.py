# 도시와 국가.
"""
매개변수로 도시 이름과 국가 이름을 받는 함수를 만들자. 이 함수는
Santiago, Chile 처럼 도시와 국가를 도시, 국가 형태의 문자열 하나로 만들어 반환해야
한다. 이 함수를 city_functions.py 모듈에 저장하자.
"""
def city_functions(city_name, country_name, population=''):
    """도시와 국가를 도시,국가 그리고 인구 형태의 문자열 하나로 만들어 반환한다."""
    if population:
        full_name = "city name: " + city_name + ' '
        full_name += "country name: " + country_name
        full_name += " -population: " + str(population)
    else:
        full_name = "city name: " + city_name + ' '
        full_name += "country name: " + country_name
    return full_name.title()
