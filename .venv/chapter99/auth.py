"""
파일명: auth.py

웰컴투파이썬 프로그램에 필요한 함수를 정의한 소스파일이다.
"""


# 메인 메뉴를 출력하는 함수
def print_main_menu():
    """
    <웰컴투 파이썬!>
    1. 회원가입
    2. 로그인
    3. 프로그램 종료
    """
    menus = ["회원가입", "로그인", "프로그램 종료"]

    print("<웰컴투 파이썬!>")
    for index, menu in enumerate(menus, start=1):
        print(f"{index}.{menu}")


# 회원가입 함수
def signup():
    pass


# 로그인 함수
def signin():
    pass


# 마이페이지를 실행하는 함수
def mypage_menu():
    pass


# 사용자 정보를 출력하는 함수
def user_info():
    pass


if __name__ == "__main__":
    print_main_menu()
