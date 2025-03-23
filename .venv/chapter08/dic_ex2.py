'''
파일명: dic_ex2.py
'''

dic_a = {
    "name": "noah",
    "age": 20
}

dic_b = {
    "name": "sonic",
    "age": 30
}

list_a = [dic_a, dic_b]
print(list_a)

# list_a 에서 dic_b 의 name과 age를 출력하세요.
my_dic = list_a[1]
print(my_dic)

print(my_dic["name"])
print(my_dic["age"])
