import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):     # ...1
    """name_function.py 테스트"""

    def test_first_last_name(self):
        """'Janis Joplin' 같은 이름이 동작하는가?"""
        formatted_name = get_formatted_name('janis', 'joplin')     # ...2
        self.assertEqual(formatted_name, 'Janis Joplin')       # ...3

    def test_first_last_middle_name(self):
        """'Wolfgang Amadeus Mozart' 같은 이름이 동작하는가?"""
        formatted_name = get_formatted_name('Wolfgang',     # ...4
            'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
"""
먼저 unittest와 테스트할 함수 get_formatted_name()을 임포트했다.
1에서는 get_formatted_name()에 사용할 단위 테스트를 묶을 NamesTestCase 클래스를
만들었다. 이 클래스 이름은 원하는 대로 지어도 되지만, 테스트할 함수와 관련되고
Test가 들어간 이름이 가장 좋다. 이 클래스는 반드시 unittest.TestCase클래스를
상속해야 파이썬이 제대로 테스트를 수행할 수 있다.

NamesTestCase에는 get_formatted_name()의 한 가지 측면을 테스트하는 단 하나의
메서드만 들어 있다. 이 메서드는 성과 이름만 들어 있는 이름이 정확한 형태로
반환되는지 확인하므로 test_first_last_name()라고 부른다. test_로 시작하는 메서드는
test_name_function.py를 실행할 때 자동으로 실행된다. 이 테스트 메서드 안에서 테스트
할 함수를 호출하고 테스트하려는 반환값을 저장한다. 이 예제에서는 get_formatted_name()
을 호출하면서 매개변수로 'jains'와 'joplin'을 넘겼고 결과는 formatted_name에
저장했다.

3에서는 unittest의 가장 유용한 기능인 단언(assert)메서드를 사용했다.
단언 메서드는 받은 결과가 예상한 결과와 일치하는지 확인한다. 여기서는
get_formatted_name()이 첫 글자를 대문자로 바꾸고 공백을 정확히 넣은 전체 이름을
반환할 것이므로 formatted_name의 값은 Janis Joplin이라고 예상한다.
이 예상이 맞는지 체크하기 위해 unittest의 assertEqual()메서드에 get_formatted_name
과 'Janis Joplin'을 넘겼다.

이행은 "formatted_name의 값과 문자열 'Janis Joplin'을 비교하라 예상대로 둘이
일치한다면 매우 좋다. 하지만 일치하지 않으면 보고하라!"라는 의미이다.

unittest.main() 행은 파이썬이 이 파일에 들어 있는 테스트를 실행하게 한다.
test_name_function.py를 실행해보자.

테스트 케이스가 통과하면 함수는 'Janis Joplin'과 같은 형태의 이름에는 여전히
동작한다는 뜻이다.

test_first_last_middle_name()메서드는 test_name_function.py를 실행할 때
메서드가 자동으로 실행되려면 메서드 이름은 반드시 test_로 시작해야 한다.
get_formatted_name()의 어던 동작을 테스트하고 있는지 명확히 드러나는 메서드
이름을 정했다. 따라서 테스트가 실패하면 어떤 종류의 이름에 문제가 생겼는지
바로 알 수 있다. TestCase 클래스의 메서드 이름은 길어도 상관없다. 테스트가 실패했을
때 출력 결과를 이해하기 쉽도록 의미 있는 이름이어야 하며, 파이썬이 이들 메서드를
자동으로 호출하므로 호출 코드를 직접 쓸 필요는 없다.

4에서는 get_formatted_name()을 호출하면서 이름과 성, 중간 이름을 넘겨 함수를 테스트
했다. 그리고 assertEqual()을 써서 반환된 전체 이름이 예상한 전체 이름(이름,
중간 이름, 성)과 일치하는지 체크했다. test_name_function.py를 다시 실행하면
두 테스트는 모두 통과한다.
"""
