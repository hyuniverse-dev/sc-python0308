'''
파일명: user_service.py
위치: chapter98/application
'''

from chapter98.domain.user import User
from chapter98.infra.user_repo import *


# 회원가입을 수행하는 함수
def sign_up():
    """
    사용자의 정보를 입력받아 저장하는 함수
    """
    try:
        id = input("아이디 >>> ")
        password = input("비밀번호 >>> ")
        name = input("이름 >>> ")
        email = input("이메일 >>> ")

        user = User(id, password, name, email)
        save(user) # 사용자 정보 저장
    except ValueError as e:
        print(f"사용자 정보 저장 실패: {e}")



if __name__ == "__main__":
    sign_up()
