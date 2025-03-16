'''
파일명: while_prac.py
'''

numbers = [1, 2, 1, 2]
value = 2

# while문을 사용해서 numbers 리스트 안의 2를 모두 지워주는 코드를 완성하세요.
while value in numbers:
    numbers.remove(value)

# numbers 리스트 출력
print(numbers)