'''
파일명: file_io_ex4.py

input() 함수 사용하기
    - 오늘 스케쥴을 관리하는 txt 파일 생성하기
    - 2025-04-05.txt 처럼 날짜를 파일명으로 저장하기
'''

import time

time_str = time.strftime("%Y-%m-%d") # 현재 날짜 데이터를 문자열로 변환
print(time_str) # 2025-04-05

file = open(f'{time_str}.txt', 'at', encoding="utf-8") # time_str 변수의 값을 사용해서 파일명 지정

while True:
    user_input = input("오늘의 스케쥴을 입력하세요 >>> ") # 사용자로부터 입력

    if not user_input: # 문자열 존재여부를 검사해서 반복여부 결정
        break # 사용자가 빈문자열 입력시 반복문 탈출

    file.write(user_input + "\n") # 입력받은 데이터를 파일에 작성

print("파일에 데이터를 작성했습니다.")
file.close()
