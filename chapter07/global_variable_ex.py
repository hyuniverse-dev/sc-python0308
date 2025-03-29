'''
파일명: global_variable_ex.py

전역 변수
    - 프로그램이 실행되는 동안 지속적으로 유지된다.
    - 지역 변수를 전역 변수에 대입하려면 global 키워드를 사용한다.
'''

value = "orange"

def global_test():
    global value
    value = "apple"
    print(value)

global_test()
print(value)
