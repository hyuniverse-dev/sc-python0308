'''
파일명: function_main_ex.py

함수 실행 파일
'''

import function4_ex
from function4_ex import find_max_min_value

# numbers = [30, 40, 50]
# max_value, min_value = find_max_min_value(numbers)
# print(max_value, min_value)

numbers = []
count = 0

while True:
    number = int(input(f"{count + 1}번째 정수를 입력하세요 (종료는 0) >>> "))

    if number != 0:
        numbers.append(number)
        count += 1
    else:
        if count < 2:
            print("최소 2개 이상의 숫자를 입력하세요.")
        else:
            break

# 함수 호출하기
max_value, min_value, = find_max_min_value(numbers)
print(f"최대값: {max_value}, 최소값: {min_value}")

