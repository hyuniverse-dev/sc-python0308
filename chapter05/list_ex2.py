'''
파일명: list_ex2.py

리스트와 함수들
'''

# 두 개의 리스트를 하나의 리스트로 연결(+ 연산자)
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
print(list_c)

# 리스트 요소를 전개하여 입력하는 것과 동일 효과(* 연산자)
list_c = [*list_a, *list_b]
print(list_c)

# 리스트 반복
list_c = list_a * 3
print(list_c)

# 리스트 길이
count = len(list_a)
print(count)

#############################

list_a = ["안", "녕", "하", "세", "요"]

# 리스트 마지막에 하나의 데이터를 추가
list_a.append("?")
print(list_a)

# 리스트의 특정 위치에 데이터를 추가
list_a.insert(5, "!")
print(list_a)

list_a.insert(2, "~")
print(list_a)

# 여러 개의 데이터를 추가
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print(list_a)

# 리스트 요소 삭제하기 - 인덱스
del list_a[0]
print(list_a)

# 리스트 요소 삭제하기 - 값
list_a.remove(6)
print(list_a)

# 리스트에 중복된 요소 존재할 때 삭제 결과
#   가장 첫 번째 매칭된 요소만 삭제된다.
list_a = [1, 1, 1]
list_a.remove(1)
print(list_a)

# 리스트의 모든 요소 제거하기
list_a.clear()
print(list_a)

# 리스트 정렬하기
#   기본은 오름차순 정렬
#   내림차순 정렬을 하려면 reverse=True 파라미터(값)를 넘겨준다.
list_a.sort(reverse=True)
print(list_a)

list_b = ["나", "다", "가", "마", "하"]
list_b.sort(reverse=True)
print(list_b)

# 리스트와 멤버쉽 연산자
#   in / not in을 사용해서 리스트에 해당 데이터가 존재하는지 확인
list_a = [1, 2, 3]
is_exist = 1 in list_a
print(is_exist)

is_exist = 1 not in list_a
print(is_exist)

# 값으로 특정 요소의 인덱스 찾기
#   리스트에 존재하지 않는 값을 찾으면 에러가 발생한다. - ValueError
idx = list_a.index(2)
print(idx)





