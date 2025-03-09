'''
파일명: if_ex2.py

다중 조건처리 주의할점
    - 다중 조건처리 시 조건의 순서에 영향을 받는다.
    - 특정 조건이 True 를 반환하면 조건문을 빠져나온다.
'''

score = 90

'''
if 60 <= score:
    print("D학점")
elif score >= 70:
    print("C학점")
elif score >= 80:
    print("B학점")
elif score >= 90:
    print("A학점")
'''

if 90 >= score:
    print("A학점")
elif 80 >= score:
    print("B학점")
# ...