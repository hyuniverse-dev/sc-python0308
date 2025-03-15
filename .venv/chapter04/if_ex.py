'''
파일명: if_ex.py

조건문
    - 주어진 조건이 참(True)이면 특정 코드를 실행한다.
    - if문, 분기문
    - indent로 실행코들 블록을 구분한다.
'''

number = 0

# number 변수의 리터럴이 0보다 크면 "양수입니다." 출력
if number > 0:
    print("양수입니다.")

print("프로그램 종료. --- (1)")

# if-else문
if number > 0:
    print("양수입니다.")
else:
    print("음수입니다.")

print("프로그램 종료. --- (2)")

# if-elif-(else) 문
if number > 0:
    print("양수입니다.")
elif number == 0:
    print("0 입니다.")
else:
    print("음수입니다.")
