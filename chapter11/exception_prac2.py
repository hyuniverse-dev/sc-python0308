'''
파일명: exception_prac2.py
'''

# 리스트 선언
numbers = [52, 273, 32, 72, 100]

# 예외처리
try:
    input_number = int(input("정수 입력 >>> "))
    print(f"{input_number}번째 요소: {numbers[input_number]}")

    # 위 코드에서 발생될 수 있는 예외 종류를 찾고
    # 각 예외를 처리하세요. 예외종류 + 예외 메세지를 출력하는 print()문 작성해주세요.
except ValueError as e:
    print(f"예외종류: {type(e)}, 메시지: {e}")
except IndexError as e:
    print(f"예외종류: {type(e)}, 메시지: {e}")
except Exception as e:
    print(f"예외종류: {type(e)}, 메시지: {e}")
