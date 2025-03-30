'''
파일명: private_var_prac.py
'''


# User 클래스 선언
class User:

    # 멤버 필드: user_id, user_password 프라이빗 변수로 선언
    #        : user_password 가 빈 문자열이면 "비밀번호는 빈문자열일 수 없습니다." 출력 user_password 에 user_id 를 대신 대입
    def __init__(self, user_id, user_password):
        self.__user_id = user_id
        if user_password:  # 빈문자열 -> False 반환 -> else 문 실행
            self.__user_password = user_password
        else:
            print("비밀번호는 빈문자열일 수 없습니다.")
            self.__user_password = user_id

    # user_password 게터와 세터
    #   : user_password 세터에는 빈 문자열인 경우 return

    def get_user_password(self):
        return self.__user_password

    def set_user_password(self, user_password):

        if not user_password:  # user_password 빈문자열 -> False -> not 연산후 True -> return
            return

        self.__user_password = user_password

################################################

# User 객체 생성
user = User("test", "1234")

# user_password 게터를 사용해서 비밀번호 출력
password = user.get_user_password()
print(password)

# user_password 세터를 사용해서 비밀번호 재할당(케이스1-빈문자열, 케이스2-새로운 비밀번호)
user.set_user_password("4321")
password = user.get_user_password()
print(password)
