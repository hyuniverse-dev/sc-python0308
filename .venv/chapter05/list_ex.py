'''
파일명: list_ex.py

리스트(list)
    - 여러가지 데이터를 저장할 수 있는 자료구조이다.
    - 독립적인 데이터만 변수에 저장했다면 리스트는 이런 데이터를 모아서 관리한다.
    - "순서가 존재" 하는 가변 자료형이다.
    - 반복이 가능한 객체이다.
'''

student_name1 = "철수"
student_name2 = "영희"
# ...
student_name1000 = "영자"

# 학생이름 여러 개를 리스트로 사용하기
student_names = ["철수", "영희", "영자", "영식"]

# 리스트명 짓는 규칙(관례)
#   - ~_list
#   - 복수형 사용

print(student_names)
numbers = [30, 10, 100, 99, -100]
floats = [3.14, 1.23, -3.14]
print(numbers)
print(floats)

mixed = [30, "철수", 180.7, 65.9]
print(mixed)

# numbers 리스트 첫 번째 요소 접근하여 출력하기
print(numbers[0])

# numbers 리스트에서 -100에 접근하여 출력하기.
print(numbers[4])

# 음수 인덱스 사용하기
print(numbers[-1])
print(numbers[-2])

# 슬라이싱
print(numbers[0:3])
print(numbers[2:4])

# 요소 수정하기
numbers[4] = 100
print(numbers)

numbers[:2] = [0, 0]
print(numbers)

# 리스트 안에 리스트
list_a = [[1, 2], [3, 4], [5, 6]]
print(list_a[0][1])
# list_a의 정수 4를 출력하기
print(list_a[1][1])

# 사실 문자열도 리스트와 동일하다.
list_b = ["apple", "banana", "cherry"]
print(list_b[0][0])
