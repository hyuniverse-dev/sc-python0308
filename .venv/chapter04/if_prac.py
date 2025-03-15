'''
파일명: if_prac.py

조건문 연습문제
'''

"""
조건문 실습1

(기획)
    사용자로부터 비밀번호를 입력받아 정합성 판단하기

(조건)
    사용자가 입력한 비밀번호와 비교할 비밀번호는 "aaa123" 입니다.

(표준입력)
    비밀번호를 입력하세요 >>>

(표준출력)
    1. 비밀번호를 입력하지 않았을 때 -> 비밀번호를 입력해주세요.
    2. 비밀번호가 일치할 때 -> 비밀번호가 일치합니다!
    3. 비밀번호가 불일치 할 때 -> 비밀번호가 불일치합니다!
"""
origin_password = "aaa123"
input_password = input("비밀번호를 입력하세요 >>> ")

''' 잘못된 예시
if origin_password == input_password:
    print("비밀번호가 일치합니다!")
elif origin_password != input_password:
    print("비밀번호가 불일치합니다!")
else:
    print("비밀번호를 입력해주세요!")
'''

if input_password == "":
    print("비밀번호를 입력해주세요!")
elif input_password == origin_password:
    print("비밀번호가 일치합니다!")
else:
    print("비밀번호가 불일치합니다!")
