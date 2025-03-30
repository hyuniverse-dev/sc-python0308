'''
파일명: raise_ex.py

예외 발생시키기
    - 강제로 특정 예외를 발생시키는 키워드
    - 특수한 상황에서 일부러 예외를 발생시켜서 뒤의 로직이 실행되지 않도록 만들어주기 위해 사용한다.
    - raise 키워드와 예외 객체를 선택해서 사용한다. 커스텀 메시지도 사용이 가능하다.
'''

user_id = "test"
user_password = "123"

try:
    if user_id != "test" or user_password != "1234":
        raise ValueError("아이디 혹은 비밀번호가 일치하지 않습니다.")
except ValueError as e:
    print(f"{e}")
