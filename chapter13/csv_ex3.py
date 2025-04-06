'''
파일명: csv_ex3.py

상품.csv 예제 리팩토링하기
'''
import csv

with open("../data/상품.csv", "rt", newline="", encoding="utf-8") as file:
    
    # csv 모듈로 읽은 file 객체를 반환
    csv_reader = csv.reader(file)

    # 헤더를 삭제 - 이터레이터를 사용하기(next())
    #   이터레이터: 반복 가능한 대상을 하나씩 반환해주는 객체이다.
    #   아래 코드에서는 첫 번째 줄을 무시하고 다음 줄로 포인터를 이동시킨다. 두 번째 줄 부터 데이터를 사용한다.
    next(csv_reader)
    data = list(csv_reader)

    total_quantity = 0
    total_price = 0

    for item in data:
        total_price += int(item[1]) * int(item[2])  # int 타입캐스팅 -> 산술연산 필요
        total_quantity += int(item[2]) # int 타입캐스팅 -> 산술연산 필요


    print(f"총 수량: {total_quantity}, 총 예상 매출: {total_price}")
