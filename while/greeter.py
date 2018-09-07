# 명확한 프롬프트 작성하기
name = input("Plese enter your name: ")
print("Hello " + name + "!")
"""
input()함수를 사용할 때는 명확하고 따라하기 쉬운 프롬프트(문장)을 써서 사용자가
여러분이 원하는 정보를 정확히 입력할 수 있도록 해야한다 사용자에게 무엇을 입력할지
알리는 문장은 무엇이든 괜찮다
"""

prompt = "IF you tell us who you are we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello " + name + "!")
