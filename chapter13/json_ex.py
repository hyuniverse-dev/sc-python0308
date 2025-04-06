'''
파일명: json_ex.py

JSON 형식
    - Javascript(언어) Object Notation Javascript 객체 표현 방법이다.
    - 주로 네트워크 통신에서 데이터를 주고 받을 때 사용한다.
    - 파이썬을 기준으로 딕셔너리와 동일한 구조로 되어 있다.
    - JSON 데이터는 속성-값(attribute-value) 쌍으로 구성된 데이터 형식이다.
    - 딕셔너리와 마찬가지로 중괄호({}) 객체를 표현한다.
        {
           "no" : 1,
           "id" : "test"
        }
'''

import json
from idlelib.iomenu import encoding

# 파이썬의 딕셔너리를 JSON 형식으로 저장
members = [
    {"no": 1, "id": "아이디1"},
    {"no": 2, "id": "아이디2"},
    {"no": 3, "id": "아이디3"},
]

with open("../data/members2.json", "w", newline="", encoding="utf-8") as file:
    # 첫 번째 파라미터: 저장할 파이썬 데이터
    # 두 번재 파라미터: 저장할 파일 객체
    # 세 번째 파라미터: (옵션) 인덴트를 추가해서 가독성 좋게 만들어준다.
    # 네 번째 파라미터: 유니코드 사용 해제 - 원문자 그대로 볼 수 있도록 저장한다.
    #                 비 ASCII 문자를 유니코드로 대체할지 지정해주는 것이다.
    json.dump(members, file, indent=4, ensure_ascii=False)

    print("members2.json 파일이 생성되었습니다.")


with open("../data/members2.json", "r", encoding="utf-8") as file:
    json_reader = file.read() # json 파일 읽어오기
    data = json.loads(json_reader) # 파이썬 자료로 변환
    print(type(data))

    for item in data:
        print(item['id'])
    

# txt 파일로 저장한 형식과 json 파일로 저장한 형식은 엄연히 다르다.
# json 형식으로 저장된 데이터는 json 모듈을 통해서 파이썬 자료구조로 사용할 수 있다.
with open("../data/members3.txt", "w", encoding="utf-8") as file:
    file.write(str(members))
    print("members3.txt 파일이 생성되었습니다.")

with open("../data/members3.txt", "r", encoding="utf-8") as file:
    read = file.read()
    print(type(read))
    print(read)






