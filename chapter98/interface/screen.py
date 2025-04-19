'''
파일명: screen.py

설명: 사용자가 사용할 화면을 출력한다.
'''
import tkinter as tk

from chapter98.application.email_service import send_lotto_numbers
from chapter98.application.lotto_service import store_numbers
from chapter98.application.user_service import sign_up


# 화면 생성 함수
def create_screen(title: str):
    GEOMETRY = "500x600"

    # 기본 창 설정
    root = tk.Tk()
    root.title(title)
    root.geometry(GEOMETRY)

    # 만들어진 창을 반환
    return root


# 회원가입 화면
def open_signup_window():
    root = create_screen("회원가입 화면")

    # 아이디 입력
    id = tk.Label(root, text="아이디를 입력하세요.")  # 레이블 생성
    id_entry = tk.Entry(root)  # 엔트리 생성(text box)
    id.pack(pady=10)  # 간격 설정(pady)
    id_entry.pack(pady=10)  # 간격 설정

    # 비밀번호 입력 (레이블: 비밀번호를 입력하세요.)
    password = tk.Label(root, text="비밀번호를 입력하세요.")
    password_entry = tk.Entry(root)
    password.pack(pady=10)
    password_entry.pack(pady=10)

    # 이름 입력 (레이블: 이름을 입력하세요.)
    name = tk.Label(root, text="이름을 입력하세요.")
    name_entry = tk.Entry(root)
    name.pack(pady=10)
    name_entry.pack(pady=10)

    # 이메일 입력 (레이블: 이메일을 입력하세요.)
    email = tk.Label(root, text="이메일을 입력하세요.")
    email_entry = tk.Entry(root)
    email.pack(pady=10)
    email_entry.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # 엔트리에 입력받은 값은 get() 함수로 가져온다.

    # 회원가입 버튼 생성
    signup_button = tk.Button(button_frame, text="회원가입", command=lambda: sign_up(
        id=id_entry.get(),
        password=password_entry.get(),
        name=name_entry.get(),
        email=email_entry.get()
    ))  # 버튼을 클릭하면 실행할 함수를 입력한다.
    signup_button.pack(side="left", pady=20)

    # 닫기 버튼 생성
    close_button = tk.Button(button_frame, text="닫기", command=lambda: root.destroy())
    close_button.pack(side="left", pady=20)

    root.mainloop()  # 해당 창을 실행하는 함수


# 로또 번호 발송 화면 생성
def open_lotto_window():
    # 화면 생성
    root = create_screen("로또 번호 발송하기")

    # receiver 입력 받기
    email = tk.Label(root, text="이메일을 입력하세요.")
    email_entry = tk.Entry(root)
    email.pack(pady=10)
    email_entry.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # 로또 번호 이메일 발송하기 버튼 생성
    lotto_button = tk.Button(button_frame, text="이메일 발송하기",
                             command=lambda: send_lotto_numbers(
                                 email_entry.get()
                             ))  # 로또 번호를 추출하여 send_email 함수 호출 + receiver 파라미터 넘기기
    lotto_button.pack(side="left", pady=100, padx=10)

    # 닫기 버튼 생성
    close_button = tk.Button(button_frame, text="닫기", command=lambda: root.destroy())
    close_button.pack(side="left", pady=20, padx=10)

    root.mainloop()


if __name__ == "__main__":
    # open_signup_window()
    open_lotto_window()
