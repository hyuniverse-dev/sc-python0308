'''
파일명: lambda_ex.py

람다

람다 함수는 이름이 없는 "익명 함수"이다. 일반적인 함수처럼 def로 정의하지 않고 lambda 키워드를 사용해서 한줄로 함수를 표현한다.
잠깐 쓰고 버리는 일회용 함수이다.

기본 구조
    lambda 매개변수: 표현식
'''


# 일반 함수 - 우선적으로 사용
def add(x: int, y: int):
    return x + y


def hello():
    return "안녕하세요"


# 람다 함수 - 필요한 경우(코드의 수를 줄이기, 특정 기능을 사용해야 할 때)
a = 10
b = 20
result = lambda x, y: x + y  # 람다 함수를 정의하고 result 식별자에 대입
print(result(a, b))  # 호출: 결과는 30을 반환한다.

result = lambda: "안녕하세요"
print(result())
