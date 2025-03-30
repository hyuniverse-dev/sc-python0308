'''
파일명: exception_ex2.py

예외 객체
    - 현실 세계에서 문제/사건 발생하면 '누가, 언제, 어디서' 라는 정보 확인
    - 프로그램 내에서는 위 정보가 예외 객체 내에 정보가 생긴다.
'''

print("== 프로그램 시작 ==")

try:
    input_number = int(input("정수 입력 >>> "))
    print(input_number / 0)
except ValueError as excpetion:
    print(f"입력하신 값이 잘못 됐습니다. ({excpetion})")
except ZeroDivisionError as exception:
    print(f"0으로는 나눌 수 없습니다. ({exception})")
except Exception as exception:
    print(f"예외가 발생했습니다. ({type(exception)}: {exception})")


print("== 프로그램 종료 ==")
