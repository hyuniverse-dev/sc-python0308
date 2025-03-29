'''
파일명: loop_extension_ex.py

중첩 반복문
    - 하나의 반복문 안에 또 다른 반복문 존재
    - 주로 중첩 리스트 혹은 중첩된 자료구조를 다룰 때 사용한다.
'''

list_a = [[1, 2, 3], [4, 5, 6]]

for item in list_a:
    for number in item:
        print(number)

i = 0

while True:
    print("바깥 while문 실행")
    # --- 1
    while True:
        print("안쪽 while문 실행")
        if i == 3:
            break
        i += 1
    # --- 2
    break

