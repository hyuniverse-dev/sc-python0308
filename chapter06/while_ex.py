'''
파일명: while_ex.py

while문
    - for문은 주어진 요소의 개수(반복하는 객체의 길이)만큼 반복을 수행하지만
      while문은 조건을 기반으로 반복을 수행한다.
    - 주어진 조건이 False이면 반복을 중단하고, True이면 반복을 계속한다.
    - 조건식이 존재한다. 만약, 조건식 계속 True 무한 반복한다 - 무한루핑
    - 조건평가에 사용되는 변수의 상태를 변화시켜줘야 한다.
'''

count = 0

while count < 5:
    print("반복할 코드 작성")
    count += 1

