'''
파일명: function_ex.py

함수
    - ~() 처럼 뒤에 식별자 뒤에 소괄호가 붙어있으면 함수라고 한다.
    - 대표적으로 print(), input(), len(), int() ...
    - 함수를 사용하는 것을 "함수를 호출한다" 고 표현한다.
    - 소괄호 안에 넣는 데이터를 인수 또는 파라미터라고 부른다.
    - 함수로부터 돌려받은 최종 값을 반환값 또는 리턴값이라고 부른다.
    - 함수는 "코드의 집합"이라고 할 수 있고, 원하는 특정 기능을 수행한다.
'''


# 내장함수 - Built-in function
#   파이썬을 설치하면 기본적으로 사용할 수 있는 함수 뜻한다.

# enumerate() - 리스트와 주로 함께 사용하고, 저장된 요소와 인덱스를 한번 반환한다.
list_a = ["a", "b", "c", "d", "e"]

for index, character in enumerate(list_a, start=1):
    print(f"현재 요소의 인덱스:{index}, 현재 요소의 데이터:{character}")

# sorted() - 정렬된 새로운 리스트를 반환해주는 함수이다.
#          - 튜플과 같이 자료구조를 변경할 수 없는 경우에 주로 사용한다.
#          - 원본을 건드리지 않고, 새로운 데이터(리스트)를 사용할 수 있다.
list_a = ["c", "a", "e", "d", "b"]
list_b = sorted(list_a, reverse=True)
print(list_a)
print(list_b)











