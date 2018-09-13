# as를 써서 모듈에 별칭 쓰기
"""
함수뿐만 아니라 모듈 이름에도 별칭을 쓸 수 있다. pizza 대신 p처럼 모듈에 별칭을
쓰면 모듈의 함수를 더 빨리 호출할 수 있다. p.make_pizza()는 pizza.make_pizza()보다
더 간결하다.
"""
import pizza1 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
import 문에서 pizza를 모듈의 별칭을 p로 정했지만, 모듈의 함수 원래 이름 그대로이다.
함수를 p.make_pizza()라고 호출하면 pizza.make_pizza()보다 더 간결할 뿐 아니라
모듈 이름에 신경 쓸 필요 없이 함수 이름에 집중할 수 있다. 이들 함수 이름은 각
함수가 무슨 일을 하든지 모듈 이름 전체를 쓸 때보다 명확하게 알리므로 코드의
가독성보다 더 중요하다.
일반적인 문법은 다음과 같다.
import module_name as mn
"""
