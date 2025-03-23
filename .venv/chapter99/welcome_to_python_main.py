'''
파일명: welcome_to_python_main.py

프로그램을 실행하는 메인 소스파일
'''

import auth

user_id = ""
user_password = ""

# 프로그램 계속 실행을 위한 무한 루프
while True:
    auth.print_main_menu()
    user_input = input("메뉴를 선택하세요 >>> ")

    if user_input == "1":
        user_id, user_password = auth.signup()
    elif user_input == "2":
        if user_id and user_password:
            # user_id != "" and user_password != ""
            is_logged = auth.isLogged(user_id, user_password)
            if is_logged:
                auth.mypage_menu()
        else:
            print("회원가입을 진행하세요.\n")
    elif user_input == "3":
        pass
    else:
        print("메뉴를 다시 선택해주세요.\n")

