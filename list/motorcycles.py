motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
"""
리스트에 항목 하나를 수정하는 문법은 리스트 항목에 접근하는 문법과 비슷하다
항목 하나를 수정할 때는 리스트 이름 다음에 바꾸려는 항목의 인덱스를 쓰고 새 값을
지정한다
"""
# 위의 예제로 motorcycles가 수정이되어서 다시 motorcycles를 정의해주었다
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') # 리스트 이름.append('값')
print(motorcycles)
"""
리스트에 새 항목을 추가해야할 경우가 많다 그럴때는 append()메서드를 이용해
원하는 항목을 추가할수있다.
"""
motorcycles=[]

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
"""
append()메서드는 리스트를 간단하게 동적으로 만들어준다 빈 리스트를 만든 다음
append()를 계속 사용해 항목을 추가할수 있다 motorcycles=[]를 빈항목으로 만들고
motorcycle을 각각 추가해주었다
"""
# insert()로 리스트에 항목 삽입하기
motorcycles.insert(0, 'ducati') #리스트 이름.insert(인덱스, 값)
print(motorcycles)
"""
insert()메서드를 이용하면 새항목을 리스트 아무 위치에다가 새로 추가할수있다
그저 새항목의 인덱스와 값을 지정해주면 된다 인덱스 0에다 인덱스로 위치해주면 원래 0
에 위치해있던 항목을 우측으로 이동해 인덱스값이 1로 자동으로 바뀐다
"""
# 리스트에서 항목 제거
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] #del 리스트 이름[제거할 항목의 인덱스]
print(motorcycles)
"""
del 문으로 리스트의 항목중 인덱스가 0인 honda를 제거해주었다
del 문으로 어떤 항목이든 지울수가 있다 del 문으로 제거한 값에는 더이상
접근할 수가 없다
"""

#pop()으로 항목 제거하기
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
"""
pop()을 써서 리스트중 suzuki 항목을 꺼내고 출력해보면 suzuki가빠진 motorcycles가
출력된다 그리고 무엇을 리스트에서 뺏는지 확인하기위해 popped_motorcycle을
출력해보면 suzuki가 출력된다
"""
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + '.')
"""
pop()메서드는 위와 같은 사용에서 유용하다 리스트의 마지막을 꺼내어 표현하고 싶을때
pop()메서드를 사용해주면 리스트에서 마지막 항목을 없어지고 다른곳에서 이용이
가능하게 된다
"""
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
"""
pop()괄호 안에 리스트 항목의 인덱스를 넣어주면 해당 인덱스 값이 꺼내어지고 사용자가
이용하고 싶은곳에 이용할수 있다. pop()으로 빼 온 항목은 리스트에서 삭제가 된다는
것을 기억하고 del문을 쓸지 pop() 메서드를 쓸지 기준은 만약 항목을 리스트에서
삭제하고 다시 쓸 일이 없으면 del문을 항목을 리스트에서 제거하고 어딘가에 사용할
목적이라면 pop()메서드를 사용하자
"""
# 값으로 항목 제거하기
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
"""
가끔 리스트에서 제거할 값의 위치를 모를 때가 있다 제거할 항목의 값을 알고있을경우
remove()메서드를 사용해서 리스트에서 제거할수 있다
"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
"""
remove()메서드는 리스트에서 제거한 값을 변수에 저장했다가 다시 사용할수 있다
만약 리스트에 동일한 값이 있을경우 remove()메서드는 가장 앞에 있는 값을 제거한다
모두 제거하고 싶으면 루프를 써야한다 나중에 알아보자
"""
