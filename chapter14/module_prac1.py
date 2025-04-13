'''
파일명: module_prac1.py

다음은 로또 번호를 추첨하는 프로그램입니다. 프로그램을 완성하세요.
'''

###### (1) random 모듈로 번호 6개 추첨하기 - 중복값 허용(1, 1, ..)
# random 모듈 추가
import random

# 번호를 담을 리스트인 numbers 초기화
numbers = []

while len(numbers) < 6:  # 루프 실행 (while문 또는 for문 선택)
    number = random.randint(1, 45)  # 난수 생성 - 1이상 45이하의 정수만 선택
    numbers.append(number)  # 생성된 난수를 numbers 리스트에 담기

# numbers 결과 출력
print(numbers)

###### (2) random 모듈로 번호 6개 추첨하기 - 중복값 미허용(1, 1, ..)

numbers = []

while len(numbers) < 6:
    number = random.randint(1, 45)

    # 중복값 미허용 조건문
    if number not in numbers:
        numbers.append(number)

print(numbers)

##### (3) random 모듈로 번호 6개 추첨하기 - 중복값 미허용(set 자료구조 사용)
#         - set은 중복값을 허용하지 않는다.
#         - 따라서 별도의 조건문이 필요하지 않다.
numbers = set()

while len(numbers) < 6:
    number = random.randint(1, 45)
    numbers.add(number)

print(list(numbers))






