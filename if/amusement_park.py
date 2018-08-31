# if-elif-else 문
"""
가능한 상황이 세 가지 이상일 때는 if-elif-else 문을 써서 이들을 평가한다 파이썬은
if-elif-else 문 중에서 단 하나의 블록만 실행한다. 각 조건은 순서대로 테스트한다
테스트가 통과하면 그 테스트 다음의 코드가 실행되며 나머지 테스트는 건너뛴다
"""
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
"""
첫 테스트에서 조건을 만족(4세 미만)하면 다음 메시지를 출력하고 나머지 테스트는
건너뛴다 elif 행은 일종의 if 테스트인데 이전 테스트가 실패해야만 실행된다 첫번째
테스트가 실패하면 이 지점에서 손님은 최소한 4세 이상이다 손님이 18세 미만이라면
아래 메시지를 출력하고 else블록은 건너뛴다 if와 elif 테스트가 모두 실패할 경우
파이썬은 else 블록의 코드를 실행한다
"""
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" +str(price) +".")
# if-elif-else 블록 안에서 바로 입장료를 출력하지 않고 저장만 한다음, 테스트가
# 끝난후 print 문을 쓰면 코드가 더 간결해진다

# elif  블록 여러개 쓰기!
"""
elif 블록은 필요한 만큼 쓸 수 있다 예를 들어 놀이 공원에서 노인 할인을 적용한다고
하면 손님이 노인인지 판단하는 조건 테스트를 코드에 추가해야한다
"""
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")
# 대부분의 코드는 그대로이다 다만 두번째 elif 블록에서 이제 손님에게 입장료 10달러
# 를 요구하기 전에 65세 미만인지부터 확인한다

# 파이썬에서 if-elif문 뒤에 else 블록은 꼭 사용할 필요는 없다 else 블록 대신에
# elif 문으로 하나 더 테스트하는 편이 원하는 조건을 찾기 쉬울 수도 있다
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age > 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
"""
else 블록을 사용할 때는 한번 더 생각해야 한다 else 블록 앞에 있는 if나 elif가
일치 하지 않았다면 else 블록이 무조건 실행되므로, 잘못된 데이터나 심지어 악의적인
데이터도 체크하지 않고 받아들일 가능성이 있다 특정 조건을 마지막으로 테스트해야
한다면 마지막에 elif 블록을 쓰고 else 블록은 생략하는 방법도 생각해보자 이렇게 하면
코드가 정확한 조건에서만 실행될 거라고 확신할 수 있다
"""
