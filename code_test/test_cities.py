import unittest
from city_functions import city_functions

class NamesTest(unittest.TestCase):
    """city_functions.py 테스트"""

    def test_city_country(self):
        """Santiago와 Chile 같은 이름이 잘 작동하는가?"""
        formatted_name = city_functions('santiago', 'chile')
        self.assertEqual(formatted_name,
            "City Name: Santiago Country Name: Chile")

    def test_city_country_population(self):
        """Santiago와 Chile 그리고 인구가 잘 작동하는가?"""
        formatted_name = city_functions('santiago', 'chile',
            population=5000000)
        self.assertEqual(formatted_name,
            "City Name: Santiago Country Name: Chile" +
            " -Population: 5000000")

unittest.main()
