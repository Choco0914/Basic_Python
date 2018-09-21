# json.dump()와 json.load()

import json

numbers =[2, 3, 5, 7, 11, 13]
filename = 'numbers.json'   # ...1
with open(filename, 'w') as f_obj:  # ...2
    json.dump(numbers, f_obj)   # ...3
"""
1에서는 숫자 리스트를 저장할 파일 이름을 정했다. 파일 확장자는 보통 .json으로 정해서
파일에 저장된 데이터가 JSON형식임을 나타낸다. 그리고 2에서 파일을 쓰기 모드로 열어
json 데이터를 파일에 저장할 수 있게 했다. 3에서는 json.dump() 함수를 써서 numbers
리스트를 numbers.json파일에 저장했다.
"""
