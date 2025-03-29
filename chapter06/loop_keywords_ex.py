'''
파일명: loop_keywords_ex.py

반복문과 대표적인 키워드
    1. break
    2. coutinue
    3. pass
'''

# break
#   주로 반복문 내부에서 사용된다.
#   실행중인 반복문을 탈출할 때(종료) 사용된다.
#   조건문은 기반으로 실행된다.

i = 0
while True:
    print(f"{i + 1}번째 반복입니다.")
    i += 1

    if i == 3:
        break

for i in range(5):
    if i == 3:
        break

while True:
    input_text = input("문자를 입력해주세요.(종료는 x 입력)")
    if input_text == "x":
        break

print("프로그램 종료")

# continue
#   현재 실행중인 반복 1번만 건너뛰기 한다.
for i in range(5):
    if i == 2:
        continue
    print(f"현재 i의 값: {i}")

# pass
#   아무런 동작을 하지 않는 더미 문장이다.
#   코드 블록을 나중에 구현할 때 또는 빈 루프나 함수를 정의를 정의할 때 사용한다.

for i in range(5):
    pass