'''
파일명: for_prac.py
'''

# 학생들의 턱걸이 횟수를 저장할 리스트 선언
record = []
students = ["현우", "지영", "동혁", "상준"]

for student in students:
    count = int(input(f"{student}(이)의 턱걸이 횟수를 입력해주세요 >>> "))
    record.append(count)

# 합계 구하기
total = sum(record)

# 평균 구하기
average = total / len(record)

# 평균 소수점 처리해서 출력하기
print(round(average))