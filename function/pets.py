# 매개변수 전달
"""
함수를 정의할 때 매개 변수를 여러 개 받도록 정의할 수 있다. 따라서 함수를 호출할 때
매개변수를 여러 개 전달할 수 있다. 함수에 매개변수를 전달하는 방법은 여러 가지다.
함수 정의에서 매개변수를 정의한 순서대로 넘기는 위치형 매개변수를 쓸 수 있고,
각 매개변수가 변수 이름과 값으로 구성되는 키워드 매개변수를 쓸 수도 있고,
리스트나 딕셔너리를 쓸수도 있다.
"""
# 위치형 매개변수
def describe_pet(animal_type, pet_name):
    """애완동물에 관한 정보를 출력한다"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
"""
첫번째 행의 함수 정의는 이 함수에 애완동물 종류와 이름이 필요함을 나타낸다.
describe_pet()을 호출할 때는 종류와 이름을 순서대로 제공해야 한다.
예를 들어 이 예제에서는 animal_type에 저장될 값 'hamster'와 pet_name에 저장될 값
'harry'를 순서대로 제공했다. 함수 본문에서는 이 두 매개변수를 써서 애완동물에 관한
정보를 표시했다.
"""
describe_pet('dog', 'willie')
# 키워드 매개변수
describe_pet(animal_type = 'hamster', pet_name= 'harry')
"""
키워드 매개변수는 함수에 넘기는 키-값 쌍이다. 매개변수 안에 이름과 값을 묶으므로
함수에 매개변수를 전달할 때 혼란스러운 일이 없다. 키워드 매개변수를 쓰면 함수를
호출할 때 순서를 걱정할 필요도 없고, 각 값의 역할이 명확히 드러난다.
describe_pet() 자체는 바뀌지 않았다. 하지만 이번에는 함수를 호출하면서 어떤
매개변수에 어떤 값을 연결할지 명시적으로 지정했다. 파이썬은 이 함수 호출을
읽으면서 'hamster'를 animal_type에, 'harry'를 pet_name에 저장해야 한다는 걸
알게된다.
"""
# 기본값
def describe_pet(pet_name, animal_type='dog'):
    """애완동물에 관한 정보를 출력한다"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
"""
함수를 만들 때 각 매개변수의 기본값을 정할 수 있다. 함수를 호출할 때 매개변수를
넘기면 파이썬은 그 값을 사용한다. 그렇지 않다면 매개변수의 기본값을 사용한다. 따라서
매개변수의 기본값을 정의 해두면 함수를 호출할 때 해당 매개변수는 생략해도 된다.
기본값을 쓰면 함수 호출이 단순해지고 함수를 사용하는 방법이 명확해진다.
위 코드에서는 첫번째 행에 animal_type 매개변수에 'dog'를 기본값으로 주었다.
"""
# 동등한 함수 호출
describe_pet('while')
describe_pet(pet_name='willie')

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
"""
위치형 매개변수와 키워드 매개변수, 기본값을 모두 함께 쓸 수 있으므로 함수 하나를
여러 가지 방법으로 호출할 수 있을 때가 많다.
함수 호출 스타일은 중요하지 않다. 원하는 결과가 나오기만 한다면 가장 이해하기
쉬운 스타일을 쓰자.
"""
# 매개변수 에러 피하기
"""
describe_pet()
Traceback (most recent call last):
  File "pets.py", line 63, in <module> ---1
    describe_pet() ---2
TypeError: describe_pet() missing 1 required positional argument: ---3
'pet_name'

함수를 쓰기 시작햇을 때 매개변수가 일치하지 않는 에러가 일어나더라고 놀라지 말아야
한다. 매개변수 불일치 에러는 함수가 동작할 때 필요한 겁소자 적거나 많은 매개변수를
저달했을 때 발생한다.
1행에는 문제의 위치가 나타나 있으므로 함수 호출을 살펴보고 무엇이 문제인지 확인할
수 있다. 2행은 무넺가 잇는 함수 이름이다. 3행은 매개변수가 한 개가 빠진
상태로 호출되었으며 빠진 매개변수가 무엇인지 알려준다.
"""
