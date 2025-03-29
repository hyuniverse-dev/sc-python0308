'''
파일명: if_ex4.py

삼항연산자
    - 세 개의 피연산자를 가지고 주어진 조건에 따라 값을 반환하는 연산자이다.
    - if - else 문과 동일한 결과를 반환한다.
    - 조건문을 축약해서 작성할 때 주로 사용한다.

삼항연산자 실행원리
    - 조건을 평가한다.
    - 조건이 True이면 좌변을 실행
    - 조건이 False이면 우변을 실행
'''

a = 10
b = 7

'''
if a > b:
    print("a가 b보다 큽니다.")
else:
    print("b가 a보다 큽니다.")

print("a가 b보다 큽니다.") if a > b else print("a가 b보다 큽니다.")
'''
message = ""

if a > b:
    message = "a가 b보다 큽니다."
else:
    message = "b가 a보다 큽니다."

print(message)


message = "a가 b보다 큽니다." if a > b else "b가 a보다 큽니다."
print(message)

