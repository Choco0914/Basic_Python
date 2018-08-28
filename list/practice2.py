invite_dinner = ['apple', 'orange', 'mango']
print('Hi ' + invite_dinner[0] + " I'm going to invite you")
print('Hi ' + invite_dinner[1] + " I'm going to invite you")
print('Hi ' + invite_dinner[2] + " I'm going to invite you")
# 손님을 초대하는 메시지
refuse_guest = invite_dinner.pop()
print(refuse_guest)
invite_dinner.append('grape')
print('Hi ' + invite_dinner[0] + " I'm going to invite you")
print('Hi ' + invite_dinner[1] + " I'm going to invite you")
print('Hi ' + invite_dinner[2] + " I'm going to invite you")
# 손님 한명이 초대를 거절해 출력해보고 다른 손님추가
invite_dinner.insert(0, 'pear')
invite_dinner.insert(2, 'tomato')
invite_dinner.append('lemon')
print('Hi ' + invite_dinner[0] + " I'm going to invite you")
print('Hi ' + invite_dinner[1] + " I'm going to invite you")
print('Hi ' + invite_dinner[2] + " I'm going to invite you")
print('Hi ' + invite_dinner[3] + " I'm going to invite you")
print('Hi ' + invite_dinner[4] + " I'm going to invite you")
print('Hi ' + invite_dinner[5] + " I'm going to invite you")
# 예약 손님을 더받을수 있다고 해서 3명을 더추가했다
refuse_message = 'Sorry I can only invite two'
print(refuse_message)
refuse_one = invite_dinner.pop()
print(refuse_one + ' '+ refuse_message)
refuse_two = invite_dinner.pop()
print(refuse_two+ ' ' + refuse_message)
refuse_three = invite_dinner.pop()
print(refuse_three + ' ' + refuse_message)
refuse_four = invite_dinner.pop()
print(refuse_four + ' '+ refuse_message)
"""
레스토랑의 농락으로 2명밖에 초대할수 없어 초대할수 없는 사람들에게 미안하다는
메시지를 보냈다
"""
print('Hi ' + invite_dinner[0] + " I'm going to invite you")
print('Hi ' + invite_dinner[1] + " I'm going to invite you")
# 초대가능한 두명에게 다시 초대메시지를 보냈다
del invite_dinner[:]
print(invite_dinner)
