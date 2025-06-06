'''
파일명: list_prac2.py
'''

# 실수 반올림 처리하기
number = 3.661592
new_number = round(number, 1)
print(new_number)


"""
A반 학생들의 턱걸이 횟수를 입력받고 학습 평균을 구하는 간단한 
프로그램을 만들어 보겠습니다. 
아래의 형식에 맞게 표준입력함수로 턱걸이 횟수 를 입력받고 
평균 턱걸이 횟수를 계산하여 
소수점 첫 번째 자리에서 반올림하여 표준출력과 동일하게 print문을 
작성하시기 바랍니다.

리스트 실습2

(기획)
    A반 학생들의 평균 턱걸이 횟수를 구하기

(표준입력)
    1. 현우의 턱걸이 횟수를 입력해주세요. >>> 
    2. 지영이의 턱걸이 횟수를 입력해주세요. >>>
    3. 동혁이의 턱걸이 횟수를 입력해주세요. >>>
    4. 상준이의 턱걸이 횟수를 입력해주세요. >>>

(표준출력)
		A반 학생들의 턱걸이 평균 : 48개
"""
# 학생들의 턱걸이 횟수를 저장할 리스트 선언
record = []

# 학생 턱걸이 횟수 입력받기
# 리스트에 횟수 저장(추가)하기
count = int(input("현우의 턱걸이 횟수를 입력해주세요 >>> "))
record.append(count)
count = int(input("지영이의 턱걸이 횟수를 입력해주세요 >>> "))
record.append(count)
count = int(input("동혁이의 턱걸이 횟수를 입력해주세요 >>> "))
record.append(count)
count = int(input("상준이의 턱걸이 횟수를 입력해주세요 >>> "))
record.append(count)

# 합계 구하기
total = sum(record)

# 평균 구하기
average = total / len(record)

# 평균 소수점 처리해서 출력하기
print(round(average))