'''
파일명: csv_ex2.py

csv 모듈 사용하기
    - CSV 형식의 파일을 다룰 때 필요한 기능이 정의되어 있는 모듈이다.
    - split() 메소드보다 편리한 기능을 추가로 제공한다.
'''
import csv

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
