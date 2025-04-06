'''
파일명: csv_ex2.py

csv 모듈 사용하기
    - CSV 형식의 파일을 다룰 때 필요한 기능이 정의되어 있는 모듈이다.
    - split() 메소드보다 편리한 기능을 추가로 제공한다.
'''
import csv

from chapter08.dic_ex4 import items

# csv 모듈로 파일 읽기
with open("../data/members.csv", "rt", encoding="utf-8") as file:
    csv_reader = csv.reader(file, delimiter=",")
    print(csv_reader)

    for item in csv_reader:
        print(item)

# csv 모듈로 파일 쓰기
with open("../data/상품.csv", "wt", newline="", encoding="utf-8") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['상품명', '가격', '수량'])
    csv_writer.writerow(['사과', 1000, 10])
    csv_writer.writerow(['바나나', 600, 20])

    print("파일이 생성되었습니다.")

# 상품.csv 파일을 읽어와서 다음 작업을 처리하세요.
#   1. 현재 상품의 총 수량을 구하세요.
#   2. 현재 상품 가격을 기준으로 상품을 모두 판매했을 때 예상 매출을 구하세요.
with open("../data/상품.csv", "rt", newline="", encoding="utf=8") as file:
    csv_reader = csv.reader(file)
    
    # 리스트 타입 캐스팅
    csv_reader = list(csv_reader) # csv_reader 객체를 list로 타입캐스팅

    total_quantity = 0
    total_price = 0

    for item in csv_reader[1:]: # 헤더를 제거하고 반복 수행
        total_price += int(item[1]) * int(item[2]) # int 타입캐스팅 -> 산술연산 필요
        total_quantity += int(item[2]) # int 타입캐스팅 -> 산술연산 필요

    print(f"총 수량: {total_quantity}, 총 예상 매출: {total_price}")