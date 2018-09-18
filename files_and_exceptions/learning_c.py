# C 배우기
"""
replace() 메서드를 써서 문자열의 단어를 다른 단어로 교체할 수 있다. 다음 문장에서
'dog'를 'cat'으로 교체하는 예제이다.

message = "I really like dogs."
message.replace('dogs', 'cat')
"""
filename = 'learning_python.txt'

with open(filename) as file_object:
    learning_python = file_object.read()
    learning_c = learning_python.replace('Python', 'c')
    print(learning_c)
