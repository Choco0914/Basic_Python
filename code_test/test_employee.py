# 직원 클래스 테스트
"""
Employee의 테스트 케이스를 만들자. 테스트 메서드 test_give_default_raise()와
test_give_default_raise()를 만들자. 각 테스트 메서드마다 새 직원 인스턴스를 만들
필요가 없도록  setup() 메서드를 사용하자. 테스트 케이스를 실행하고 두 테스트가
모두 통과하는지 확인해라.
"""
import unittest
from employee import Employee

class TestEmplyee(unittest.TestCase):
    """직원의 정보를 표시하는 Employee 클래스를 테스트한다."""

    def setUp(self):
        """메서드에 사용하는 인스턴스를 생성한다."""
        self.eric = Employee('eric', 'matthes', 65000)

    def test_give_default_raise(self):
        """기본 연봉의 값을 지정한다."""
        self.eric.given_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_default_raise(self):
        """임의적으로 연봉의 값을 지정하는 테스트"""
        self.eric.given_raise(10000)
        self.assertEqual(self.eric.salary, 75000)


unittest.main()
