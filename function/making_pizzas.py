# 함수를 모듈에 저장 전체 모듈 임포트하기
"""
함수의 장점 중 하나는 코드 블록을 메인 프로그램에서 분리할 수 있다는 것이다.
함수에 의미 있는 이름을 쓰면 메인 프로그램을 읽기가 훨씬 쉬워진다. 함수를 따로
저장한 파일을 모듈(module)이라고 하며, 이 모듈을 메인프로그램에서 임포트(import)
해서 이 장점을 더 확대 할 수 있다. import 문은 파이썬이 모듈의 코드를 읽고 현재
코드 실행 중인 프로그램 파일에서 사용할 수 있게 한다.
"""
import pizza1

pizza1.make_pizza(16, 'pepperoni')
pizza1.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
파이썬은 이 파일을 읽으면서 import pizza 행에서 pizza1.py 파일을 열고 그 파일에
있는 모든 함수를 이 프로그램에 복사한다. 파이썬은 프로그램이 실행됨에 따라 이면에서
코드를 복사하므로 실제로 코드가 복사된 것처럼 보이지는 않는다. 우리는 그저 pizza1.py
파일에 저의된 함수를 모두 making_pizzas.py 파일에서 쓸수 있다는 것만 알면 된다.

이렇게 키워드 import를 쓰고 그 다음에 모듈 이름을 쓰는 임포트 방법은 모듈의 모든
함수를 프로그램에서 쓸 수 있게 한다. 이렇게 import 문을 써서 moduel_name.py 모듈
전체를 임포트하면 모듈의 각 함수는 다음 문법에 따라 사용한다.
module_name.function_name()
"""
# 특정 함수만 임포트하기
"""
모듈에서 특정 함수만 임포트할 수도 있다. 이 방법은 보통 다음과 같은 문법을 쓴다.
from module_name import function_name
각 함수 이름을 쉼표로 구분해 함수를 원하는 만큼 임포트할 수도 있다.
from module_name import function_0, function_1, function_2
"""
from pizza1 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
위와 같은 문법을 쓰면 호출할 때 점 표기법을 쓰지 않아도 된다. 즉, 모듈 전체를
호출했을때는 module_name.function_name()처럼 사용했지만 위 처럼 임포트하게 되면
function_name()만 사용할 수 있다. 앞의 import 문에서 명시적으로 make_pizza()
함수를 임포트했으므로 함수 이름만으로 호출할 수 있다.
"""
