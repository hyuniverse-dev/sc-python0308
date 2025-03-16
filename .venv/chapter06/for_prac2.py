'''
파일명: for_prac2.py
'''

"""
다음 빈칸을 채워서 리스트 요소 중 100 이상의 숫자만 출력하게 프로그램을 완성하세요.
"""
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print(number)

"""
다음 빈칸을 채워서 리스트 요소의 홀/짝을 판별하는 프로그램을 완성하세요.
"""

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} 는 짝수입니다.")
    else:
        print(f"{number} 는 홀수입니다.")

print()

"""
2번 문제를 while문으로 변경하기
"""

index = 0

while index < len(numbers):

    number = numbers[index]

    if number % 2 == 0:
        print(f"{number} 는 짝수입니다.")
    else:
        print(f"{number} 는 홀수입니다.")

    index += 1
