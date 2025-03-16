'''
파일명: range_ex.py

범위 자료형
    - 대표적으로 for문과 함께 많이 사용되는 범위 자료형이다.
'''

numbers = list(range(1000))
print(numbers)

for number in range(2):
    print(number)

for number in range(1, 3):
    print(number)

for number in range(1, 11, 2):
    print(number, end=", ")