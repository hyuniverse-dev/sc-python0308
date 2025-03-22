'''
파일명: function3_ex.py

return 문 (반환문)
    - return 키워드는 함수 내부에서 사용할 수 있다.
    - 이 키워드는 함수를 실행했던 호출자로 돌아가라는 뜻이다.
    - 주로 함수가 끝나는 구간에 위치한다.
'''

def return_test():
    print("1번 위치입니다.")
    return
    print("2번 위치입니다.")


return_test()

def return_test2():
    print("== hello return_test2 ==")
    return 100

res = return_test2()
print(res)

def return_list(some_list: list):
    """
    이 함수는 함수 단원에서 다양한 자료구조를 매개변수와 반환값으로
    사용할 수 있다는 예제이다.

    :param some_list: 특정 리스트를 매개변수로 받는다.
    :return: 새로운 데이터가 추가된 리스트를 반환한다.
    """
    some_list.append("새로운 데이터")
    return some_list

list_a = ["기존 데이터1", "기존 데이터2", "기존 데이터3"]
res = return_list(list_a)
print(res)

def add(number1, number2):
    return number1 + number2


