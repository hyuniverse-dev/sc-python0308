'''
파일명: if_prac5.py
'''

name = input("학생의 이름을 입력하세요 >>> ")
korean = int(input("국어 점수 >>> "))
english = int(input("영어 점수 >>> "))
math = int(input("수학 점수 >>> "))
is_valid = True

if not (0 <= korean <= 100):
    is_valid = False
    print(f"국어 점수입력 오류입니다. (입력값: {korean})")

if not (0 <= english <= 100):
    is_valid = False
    print(f"영어 점수입력 오류입니다. (입력값: {english})")

if not (0 <= math <= 100):
    is_valid = False
    print(f"수학 점수입력 오류입니다. (입력값: {math})")

if is_valid:
    total = korean + english + math
    average = total / 3

    if average >= 80:
        print("보충학습 대상이 아닙니다.")
    else:
        diff = 80 - average
        print(f"보충학습 대상입니다.(점수차: {diff})")
