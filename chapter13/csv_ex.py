'''
파일명: csv_ex.py

CSV 파일 다루기
    - CSV 형식은 데이터를 '쉼표'로 분리하여 관리한다.
    - 보통 데이터베이스나 스프레드시트에서 사용할 수 있는 형식이다.

CSV 파일 읽기
    - split() 메소드를 활용해서 데이터를 추출하는 방법이 존재한다.
    - split() 메소드는 특정 구분자에 따라서 값을 분리하고 리스트로 반환한다.
'''

alpha = "a,b,c,d,e"
res = alpha.split(",")
print(res)

members = []

with open("../data/members.csv", "rt", encoding="utf-8") as file:
    data = file.readlines()
    # "회원번호,아이디,이름"
    print(data)
    for item in data:
        item = item.split(",")  # ["회원번호", "아이디", "이름"]
        print(item)
        members.append(item)

# 회원의 이름만 리스트로 모아서 출력하세요.
# 회원번호 / 아이디를 각각 리스트로 모아서 출력하세요.
names = []
ids = []
numbers = []

for member in members[1:]:
    numbers.append(member[0])
    ids.append(member[1])
    names.append(member[2])

print(numbers)
print(ids)
print(names)

# csv 파일이 아닌 다른 구분자로 데이터가 구분되어 있을 때 - split() 사용의 확장
alpha = "a/b/c/d/e"
phone_number = "010-123-1234"

alpha_split = alpha.split("/")
phone_number_split = phone_number.split("-")

print(alpha_split)
print(phone_number_split)

star = len(phone_number_split[1]) * "*"
phone_number = f"{phone_number_split[0]}-{star}-{phone_number_split[2]}"
print(phone_number)
