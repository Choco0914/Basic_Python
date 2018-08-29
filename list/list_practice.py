# ex1
for value in range(1, 21):
    print(value)
milion = list(range(1, 1000001))
#for number in milion:
#    print(number)
# 1000000까지 출력하는 시간이 너무길어 주석처리했다
print(max(milion))
print(min(milion))
print(sum(milion))
# 홀수를 출력
odd_numbers = list(range(1, 20, 2))
for odd in odd_numbers:
    print(odd)
#3 의 배수 출력
three_numbers = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for three in three_numbers:
    print(three)
three_squares = list(range(1, 11))
for three in three_squares:
    value = three**3
    print(value)
three_comprehension = [value**3 for value in range(1, 11)]
print(three_comprehension)
