'''
파일명: dic_ex4.py
'''

my_dic = {
    "name": "my_name",
    "gender": "male",
    "job": "student"
}

check_key = "name"

if check_key in my_dic:
    print(f"{check_key}가 {my_dic} 안에 존재합니다.")

# 매번 in 연산을 통해서 key를 확인하기 어려운 경우는
# get() 함수를 사용해서 데이터를 찾는다.
# 키가 없는 경우 기본으로 None을 반환하고, 기본값을 설정하면 해당 값을 반환한다.

# age = my_dic["age"]
age = my_dic.get("age", 0)
print(f"나의 나이는: {age}세 입니다.")
print(my_dic)

# len()
#   딕셔너리 안의 키-값 쌍의 수를 반환한다.
length = len(my_dic)
print(length)

# copy()
#   딕셔너리를 "얕은복사" 한다.
new_dic = my_dic.copy()
print(my_dic)
print(new_dic)

#####

# items()
#   모든 키-값 쌍을 튜플 형태로 반환한다.
items = my_dic.items()
print(items)

# keys()
#   모든 키를 리스트 형태로 반환한다.
keys = my_dic.keys()
print(keys)

# value()
#   모든 값을 리스트 형태로 반환한다.
values = my_dic.values()
print(values)

# setdefault()
#   지정된 키에 대한 값을 반환하는데
#   키가 없는 경우 기본값을 추가한다.
#   원본 딕셔너리를 변경한다.
age = my_dic.setdefault("age", 0)
print(f"나의 나이는: {age}세 입니다.")
print(my_dic)

# clear()
#   딕셔너리 안의 모든 요소를 제거한다.
my_dic.clear()
print(my_dic)
