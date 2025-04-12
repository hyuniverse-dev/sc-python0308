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
        has_alpha = False
        has_digit = False
        for char in password:
            if char.isalpha():
                has_alpha = True
            if char.isdigit():
                has_digit = True

        if not has_alpha or not has_digit:
            raise ValueError("비밀번호는 영어와 숫자의 조합이어야 합니다.")

        self.id = id
        self.password = password
        self.name = name
        self.email = email


if __name__ == "__main__":
    user = User("test", "abcd1234", "noah", "test@email.com")
    print(user.name, user.email, user.id)
