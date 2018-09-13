# as를 써서 함수에 별칭 붙이기
"""
임포트하려는 함수 이름이 프로그램의 기존 이름과 충돌하거나 너무 길다면, 짧고 고유한
별칭(alias)을 쓸 수 있다. 별칭은 일종의 함수 별명이다.
"""
from pizza1 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra chesse')
