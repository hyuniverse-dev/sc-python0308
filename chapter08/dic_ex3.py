'''
파일명: dic_ex3.py
'''

dic_a = {
    "name": "noah"
}
print(dic_a)

# 딕셔너리에 존재하지 않는 키에 접근하면 자동으로 추가해준다.
dic_a["age"] = 20
print(dic_a)

# 딕셔너리에 존재하는 키에 접근하여 새로운 값을 대입하면 수정된다.
dic_a["age"] = 21
print(dic_a)

# 딕셔너리에 특정 키와 값 삭제하기
del dic_a["age"]
print(dic_a)

# 딕셔너리 주의할 점
#   딕셔너리에 존재하지 않는 키에 접근하면 KeyError 가 발생한다.
# print(dic_a["hobbies"])


dic_a = {
    "name" : "noah"
}

dic_b = {
    "name" : "sonic",
    "age" : 20
}

list_a = [dic_a, dic_b]

# dic_a 에 접근해서 age 키로 21 정수 데이터를 추가해주세요.
dic_a = list_a[0]
dic_a["age"] = 21
print(dic_a)

# dic_b 에 접근해서 name 키의 데이터를 chad 로 수정해주세요.
dic_b = list_a[1]
dic_b["name"] = "chad"
print(dic_b)

# dic_b 에 접근해서 age 키의 데이터를 제거해주세요.
del dic_b["age"]
print(dic_b)

# list_a 의 결과 출력
print(list_a)













