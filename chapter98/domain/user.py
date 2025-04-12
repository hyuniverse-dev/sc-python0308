'''
파일명: user.py
위치: chapter98/domain/
'''


class User:

    def __init__(self, id: str, password: str, name: str, email: str):

        # 이메일 정합성 검사 ('@', '.' 기호만 존재하면 된다.)
        if "@" not in email or "." not in email:
            raise ValueError("이메일 형식이 올바르지 않습니다.")
        
        # 비밀번호 영어 + 숫자 조합 검사

        self.id = id
        self.password = password
        self.name = name
        self.email = email
