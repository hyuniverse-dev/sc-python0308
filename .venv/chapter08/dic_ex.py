'''
파일명: dic_ex.py

딕셔너리(Dictionary)
    - 리스트는 인덱스를 기반으로 값을 관리하는 자료구조라면,
      딕셔너리는 "키(key)"를 기반으로 값을 관리하는 자료구조이다.
    -
'''

dic_a = {
    "이름": "노아",
    "성별": "남자",
    "나이": 20,
    "취미": ["독서", "공부하기", "운동하기", "숨쉬기"],
    "상세정보": {
        "키": 180,
        "몸무게": 60,
        "시력": 2.0
    }
}

name = dic_a["이름"]
print(name)

hobbies = dic_a["취미"]
print(hobbies)

details = dic_a["상세정보"]
print(details)

height = details["키"]
print(height)

height = dic_a["상세정보"]["키"]
print(height)

dic_a = {
    "name" : "noah",
    "gender" : "male",
    "hobbies" : ["playing", "sleeping", "eating"]
}

print(dic_a["name"])

# 자주 실수하는 케이스
dic_a = {
    name : "noah",
    gender : "male",
    hobbies : ["숨쉬기", "독서하기"]
}

# print(dic_a["name"]) # NameError 발생










