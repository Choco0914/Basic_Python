buffets = ('초밥', '갈비', '소고기', '케잌', '국수')
for buffet in buffets:
    print(buffet)
"""
buffets[2] = '레몬'
Traceback (most recent call last):
  File "buffet.py", line 4, in <module>
    buffets[2] = '레몬'
TypeError: 'tuple' object does not support item assignment
"""
print('\n')
buffets = ['초밥', '갈비', '소고기', '비빔면', '만두']
for buffet in buffets:
    print(buffet)
