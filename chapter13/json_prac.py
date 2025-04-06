'''
파일명: json_prac.py
'''
import json

products = [
    {
        "name": "사과",
        "price": 1000,
        "quantity": 10
    },
    {
        "name": "바나나",
        "price": 800,
        "quantity": 5
    }
]

# 위의 products 를 상품2.json 파일 형식으로 저장
with open("../data/상품2.json", "w", encoding="utf-8") as file:
    json.dump(products, file, indent=4, ensure_ascii=False)
    print("상품2.json 파일이 생성되었습니다.")

# 상품2.json 파일을 읽어서 바나나를 다 판매했을 때 예상 매출을 구하세요.
#   - 읽어온 데이터는 list 일 것이다. 순회해서 "name"이 "바나나"인 경우 price * quantity
with open("../data/상품2.json", "r", encoding="utf-8") as file:
    json_reader = file.read()
    data = json.loads(json_reader) # 파이썬 자료 구조로 변환
    
    # 상품리스트를 반복하면서 바나나 찾기
    for item in data:
        name = item.get("name", "")
        price = item.get("price", 0)
        quantity = item.get("quantity", 0)

        # 반복중인 딕셔너리의 'name' 이 '바나나'이면 예상 매출 계산
        if name == "바나나":
            total_price = price * quantity
            print(f"바나나의 예상 매출: {total_price}")















