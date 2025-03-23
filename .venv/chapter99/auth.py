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


# 마이페이지 메뉴를 출력하는 함수
def print_mypage_menu():
    """
    1. 회원정보 조회
    2. 회원 탈퇴하기
    3. 홈으로
    """
    # 마이페이지 메뉴 리스트 생성
    menus = ["회원정보 조회", "회원 탈퇴하기", "홈으로"]
    print("<마이페이지>")
    # 반복문을 사용해서 메뉴 출력
    for index, menu, in enumerate(menus):
        print(f"{index}.{menu}")


# 회원가입 함수
def signup():
    input_id = input("아이디를 입력하세요 >>> ")
    input_password = input("비밀번호를 입력하세요 >>> ")

    if input_id and input_password:
        print("회원가입이 완료되었습니다.")
    else:
        print(f"아이디와 비밀번호를 확인해주세요. (아이디:{input_id} / 비밀번호:{input_password})")

    return input_id, input_password


# 로그인 함수
def signin(user_id: str, user_password: str):
    input_id = input("아이디를 입력하세요 >>> ")
    input_password = input("비밀번호를 입력하세요 >>> ")

    # 입력받은 데이터와 저장된 데이터가 모두 같으면 "로그인 되었습니다!"
    # 입력받은 데이터와 저장된 데이터가 다르면 "아이디 혹은 비밀번호가 일치하지 않습니다!"
    if user_id == input_id and user_password == input_password:
        print("로그인 되었습니다!")
        return True
    else:
        print("아이디 혹은 비밀번호가 일치하지 않습니다.")
        return False


# 마이페이지를 실행하는 함수
def mypage_menu():
    while True:
        print_mypage_menu()
        user_input = input("메뉴를 선택하세요 >>> ")

        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            break
        else:
            print("메뉴를 다시 선택해주세요.\n")


# 사용자 정보를 출력하는 함수
def user_info():
    pass


if __name__ == "__main__":
    # print_main_menu()
    signup()
