'''
파일명: for_ex.py

반복문을 사용하는 이유
    - 반복되는 작업을 수행하기 위해 사용한다.
    
for문
    - 반복 가능한 대상(iterable한 객체)를 순회하는데 사용되는 반복문이다.
    - 리스트, 문자열, 튜플, 딕셔너리 등이 반복 가능한 대상이다.
    - 반복할 요소가 없으면 자동으로 반복문 종료된다.
'''

colors = ["red", "green", "blue"]

for color in colors:
    print(color)

word = "apple"

for alpha in word:
    print("-", alpha)