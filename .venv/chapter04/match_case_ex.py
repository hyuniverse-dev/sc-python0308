'''
파일명: match_case_ex.py

match-case 문
    - if 문은 조건을 기반으로 True/False 에 따라 분기처리
    - match-case 문은 주어진 값의 패턴에 따라 분기처리
'''

value = 40

match value:
    case 40:
        print("정수 40입니다.")
    case 30:
        print("정수 30입니다.")
    case 20:
        print("정수 20입니다.")

if value == 40:
    print("정수 40입니다.")
elif value == 30:
    print("정수 30입니다.")
elif value == 20:
    print("정수 20입니다.")

value = "C"

match value:
    case "Python":
        print("파이썬 수업 입니다.")
    case "Java":
        print("자바 수업 입니다.")
    case _: # 언더바(_) == else 와 동일한 기능(와일드카드)
        print("존재하지 않는 과목명입니다.")

if value == "Python":
    print("파이썬 수업 입니다.")
elif value == "Java":
    print("자바 수업 입니다.")
else:
    print("존재하지 않는 과목명입니다.")









