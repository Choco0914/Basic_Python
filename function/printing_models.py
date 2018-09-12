# 함수에서 리스트 수정하기
"""
사용자가 전송한 디자인을 3D 프리넡로 출력하는 회사가 있다. 출력한 디자인은
리스트에 저장되고, 출력 후에는 별도의 리스트에 저장된다.
"""
# 출력할 디자인으로 시작한다.
unprinted_designs = ['iphon case', 'robot pendant', 'dodecahedron']
completed_models = []

# 남은 것이 없을 때까지 각 디자인의 출력을 시뮬레이트 한다.
# 출력한 각 디자인을 completed_models로 옮긴다.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #디자인에서 3D 출력 시뮬레이트
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#출력이 끝난 모델 모두 표시
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
print("\n")
"""
위 프로그램은 출력할 디자인 리스트 unprinted_designs와 출력이 끝난 각 디자인을
저장할 빈 리스트 completed_models에서 시작한다. unprinted_designs에 디자인이
남아잇는 한 while 루프는 각 디자인을 리스트 마지막에서 꺼내 current_design에
저장하며 현재 디자인을 출력 중이라는 메세지를 표시하는 방식으로 디자인 출력을
시뮬레이트 한다. 그리고 그 디자인을 출력이 끝난 모델 리스트에 추가한다.
루프가 끝나면 디자인 리스트가 표시된다.
"""
def print_models(unprinted_designs, completed_models):
    """
    남은 것이 없을 때까지 각 디자인의 출력을 시뮬레이트한다.
    출력한 각 디자인을 completed_models로 옮긴다.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 디자인에서 3D 출력 시뮬레이트

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_complted_models(completed_models):
    """출력이 끝난 모델 모두 표시"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphon case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_complted_models(completed_models)
"""
위 프로그램은 함수를 쓰지 않은 버전과 같은 결과를 출력하지만, 코드는 훨씬 더
정리되어 있다. 대부분의 작업을 수행하는 코드를 두 함수로 분리해서 프로그램의 주요
부분을 이해하기 쉽게 만들었다. 프로그램 바디를 보고, 이 프로그램의 기능을 이해하는
것이 얼마나 쉬워졌는지 보자.
출력하지 않은 디자인 리스트와 출력이 끝난 디자인을 담을 빈 리스트를 정의했다.
함수 두 대를 이미 정의했으므로 이제 필요한 일은 함수를 호출하면서 정확한 매개변수를
전달하는 것 뿐이다.print_models()를 호출하면서 두 가지 리스트를 전달하면
print_models()는 예상대로 디자인 출력을 시뮬레이트한다. 다음에는
show_complted_models()을 호출하면서 출력이 끝난 디자인 리스트를 전달해 출력된
디자인을 보고하게 했다 의미 있는 함수 이름을 썼으므로 설령 주석이 없더라도
다른 사람이 이 코드를 보고 이해할 수 있다.

이 프로그램은 함수를 쓰지 않은 버전보다 확장하고 관리하기 쉽다. 나중에 다른 디자인을
더 출력하더라도 단순히 print_models()를 다시 호출하기만 하면 된다. 출력 코드를
수정해야 할 때 코드를 한 번만 수정하면 함수를 호출할 때마다 수정한 코드가 사용된다.
프로그램의 이곳 저곳에 흩어진 코드를 수정하는 것보다는 훨씬 효율적이다.

모든 함수가 특정한 작업 한 가지를 수행해야 한다는 점도 알게되었다. 첫 번째 함수는
각 디자인을 출력하고, 두 번째 함수는 출력이 끝난 모델을 표시한다. 함수 하나에서
두 가지 일을 다 하게 만드는 것보다는 이 방법이 더 낫다. 함수가 너무 많은 작업을
한다고 생각하면 함수를 두 개로 나눠 보자. 함수에서 다른 함수를 호출할 수 있으므로
복잡한 작업을 몇 단계로 나누기 쉽다.
"""
# 함수가 리스트를 수정하지 못하게 막기
def print_models(unprinted_designs, completed_models):
    """
    남은 것이 없을 때까지 각 디자인의 출력을 시뮬레이트한다.
    출력한 각 디자인을 completed_models로 옮긴다.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 디자인에서 3D 출력 시뮬레이트

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_complted_models(completed_models):
    """출력이 끝난 모델 모두 표시"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphon case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_complted_models(completed_models)
print(unprinted_designs)
