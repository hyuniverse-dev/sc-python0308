'''
파일명: user_repo
위치: chapter98/infra/
'''
from chapter98.domain.user import User
import json


# 유저 정보를 저장하는 함수
def save(user: User):
    file_path = "C:/sc-python0308-main/data/users.json"

    user = user.__dict__  # 객체의 메소드를 제외한 속성만을 딕셔너리로 반환
    print(f"user: {user}")

    save_data_tojson(file_path=file_path, data=user)


# 공통 함수 -> JSON 파일에 데이터를 저장할 때 공통으로 호출해서 사용하는 함수
def save_data_tojson(file_path: str, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file_path, indent=4, ensure_ascii=False)
    print(f"{file_path}에 파일이 생성/저장 되었습니다.")
