'''
파일명: module_ex1.py

- 내장 모듈
    기본적으로 사용할 수 있는 모듈
    math, random, datetime 등..
'''

# math
import math

# pi 값 사용하기
pi = math.pi
print(pi)
print(round(pi, 2))

# 올림
print(math.ceil(pi))

# 내림
print(math.floor(pi))

# 제곱근
print(math.sqrt(25))

# ** 제곱연산자 대체
print(math.pow(5, 2))

# random 모듈
import random

# randint()
#   1 이상 10 이하의 정수를 무작위로 반환
result = random.randint(1, 10)
print(result)

# randrange()
#   1 이상 10 미만의 정수를 무작위로 반환
result = random.randrange(1, 10)
print(result)

# 확률로 아이템 뽑기
items = ["전설의 검", "날이 무딘 검", "칼자루만 남은 검", "칼집"]

# 0 이상 1미만의 범위에서 임의의 실수를 생성하는 random() 를 사용한다.
probability = random.random()

if probability < 0.1:
    item = items[0]
elif probability < 0.3:
    item = items[1]
else:
    item = items[3]

print(f"{item}을 획득했습니다. (확률O)")

# choice() - 확률과 무관하게 임의로 리스트에서 하나의 요소만 반환
item = random.choice(items)
print(f"{item}을 획득했습니다. (확률X)")

# datetime 모듈
import datetime

# from datetime import datetime -> now()만 사용하는 경우 이 형식을 자주 사용한다.

now = datetime.datetime.now()
print(now)

# date()
result = datetime.date(2025, 4, 13)
print(result)

# time()
result = datetime.time(10, 00, 00)
print(result)

# 특정 날짜에서 원하는 데이터(연/월/일/시간정보)를 추출할 때
print(f"현재 연도: {now.year}")
print(f"현재 월: {now.month}")
