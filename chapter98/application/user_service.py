'''
파일명: user_service.py
위치: chapter98/application
'''

from chapter98.domain.user import User
from chapter98.infra.user_repo import *
from chapter99.auth import signin


# 회원가입을 수행하는 함수
def sign_up():
    try:
        id = input("아이디 >>> ")
        password = input("비밀번호 >>> ")
        name = input("이름 >>> ")
        email = input("이메일 >>> ")

        user = User(id, password, name, email)
        save(user)  # 사용자 정보 저장
    except ValueError as e:
        print(f"사용자 정보 저장 실패: {e}")


# 로그인을 수행하는 함수
def sign_in():
    id = input("아이디 >>> ")
    password = input("비밀번호 >>> ")

    try:
        user = find(id, password)
        print(user)
        if user:
            print(f"회원이름: {user.name}")
        else:
            print("조회된 사용자가 없습니다.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    # sign_up()
    sign_in()
