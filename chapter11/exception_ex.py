'''
파일명: exception_ex.py

예외처리
    - 구문 오류 / 실행 오류(예외)

구문 오류
    - 들여쓰기, 문법적 오류 등

실행 오류
    - 데이터에 따라 발생하는 오류
    - 로직 처리를 제대로 하지 못했을 때 발생

try - except 문
    - try 블록에는 예외가 발생할 가능성이 있는 코드를 작성한다.
    - except 블록에는 예외가 발생했을 때 처리할 코드를 작성한다.

else 문
    - 예외가 발생하지 않을 때 추가로 실행된다.

finally 문
    - 예외 발생여부 상관업시 무조건 실행된다.

예외 처리 구문 조합
    - try + except
    - try + except + else
    - try + except + finally
    - try + except + else + finally
    - try + finally
    - (안되는 구문) try + else
'''
from typing import final

# 구문오류
# print(Hello, World!)

# 실행오류(예외)
list_a = []
print("== 프로그램 실행 ==")
if len(list_a) > 2:  # 전통적인 예외처리 방법
    print(list_a[1])

# try - except 문
try:
    # 예외 발생 가능성이 있는 코드를 작성하는 부분
    radius = int(input("반지름을 입력 >>> "))

    print(f"반지름 : {radius}")
    print(f"원의 넓이 : {3.14 * (radius ** 2)}")
except:
    # 예외가 발생했을 때 처리할 코드를 작성하는 부분
    # pass -> 별 다른 처리를 하지 않을땐 더미문장 사용한다.
    print("예외가 발생했을 때 실행되는 코드")
else:
    print("예외가 없을 때 추가로 실행되는 코드")
finally:
    print("예외가 발생하던 / 안하던 무조건 실행되는 코드")

print("== 프로그램 종료 ==")
