'''
파일명: operator.py

설명
    - 연산자의 종류를 학습한다. 연산의 결과를 예측하고, 실제 연산된 결과 비교해야 한다.
    - 기대 결과를 제어할 수 있어야 한다.
    - 연산의 우선순위, 적당한 연산자를 선택
'''

# 대입연산자(할당연산자)
#   특정 변수에 값을 할당하는데 사용되는 연산자이다.
subject = "파이썬"

# 산술연산자
#   더하기, 빼기, 곱하기, 나누기, 몫, 나머지, 제곱
x = 5
y = 2

print(x + y)  # 더하기
print(x - y)  # 빼기
print(x * y)  # 곱하기
print(x / y)  # 나누기
print(x // y)  # 몫만
print(x % y)  # 나머지만
print(x ** y)  # 제곱

# 산술연산자(문자열 연산)
#   문자열 데이터는 더하기, 곱하기 연산만 가능하다.
tag1 = "#파이썬"
tag2 = "#신촌"
tag3 = "#주말반"

tag = tag1 + tag2 + tag3
print(tag)

message = "화이팅!" * 3
print(message)

# 복합대입연산자(복합할당연산자) - 대입연산자 + 산술연산자를 복합적으로 사용한다.
#   기존 변수 값을 가져와서 연산 후에 다시 해당 변수에 저장하는 작업을 단축시켜준다.
x = 5
x += 3  # x = x + 3
print(x)

x -= 3  # x = x - 3
print(x)

x *= 2  # x = x * 2
print(x)

x /= 2  # x = x / 2
print(x)

# 관계연산자(비교연산자)
#   등호, 부등호, 크다, 크거나 같다, 작다, 작거나 같다
#   비교한 값의 결과를 불린으로 반환한다. (True / False)
#   조건문, 논리 연산자와 자주 사용된다.
x = 5
y = 2
print(x == y)  # 같다 -> False
print(x != y)  # 다르다 -> True
print(x > y)  # x가 y보다 크다 -> True
print(x >= y)  # x가 y보다 크거나 같다 -> True
print(x < y)  # x가 y보다 작다 -> False
print(x <= y)  # x가 y보다 작거나 같다 -> False

# 관계연산자(문자열 데이터)
print("파이썬" == "파잇썬")
print("파이썬" != "파잇썬")

# 논리연산자
#   두 개 이상의 논리적인 조건을 조합할 때 사용되는 연산자이다.
#   and(그리고), or(또는), not(부정)
#   not 연산자가 우선순위가 가장 높습니다.
x = 5
y = 2
print(1 < x and x < 10)
print(3 < y and y < 10)

print(1 < x or x < 10)
print(3 < y or y < 10)

print(not True)
print(not False)

# 논리연산자 퀴즈
print((1 < 5) and (2 < 5) and (3 < 5))  # True
print(True and False)  # False
print((1 > 5) and (2 > 5) and (3 > 5))  # False

# 논리연산자 우선순위 비교
print(not True and False or not False)

# 멤버십 연산자
#   특정 문자열 내에 해당 문자열이 존재하는지 판별
#   in, not in
print("a" in "abc")
print("z" not in "abc")
print("cb" in "abc")

email = "test@naver.com"
print("@" in email)



