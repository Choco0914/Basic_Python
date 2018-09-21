# json.dump()와 json.load()
import json

filename = 'numbers.json'   # ...1
with open(filename) as f_obj:   # ...2
    numbers = json.load(f_obj)  # ...3

print(numbers)
"""
1에서는 위에서 저장한 파일을 불러오게 지정했다. 이번에는 2에서 파일을 읽기 모드로
열었다. 3에서는 json.load() 함수를 써서 numbers.json에 저장된 정보를 numbers 변수에
저장했다. 마지막으로 숫자 리스트를 출력해 numbers_writer.py와 같은 리스트인지
확인했다.
"""
