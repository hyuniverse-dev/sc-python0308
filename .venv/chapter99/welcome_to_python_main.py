'''
파일명: welcome_to_python_main.py

프로그램을 실행하는 메인 소스파일
'''

import auth

# 프로그램 계속 실행을 위한 무한 루프
while True:
    auth.print_main_menu()
    user_input = input("메뉴를 선택하세요 >>> ")

    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    else:
        print("메뉴를 다시 선택해주세요.\n")

