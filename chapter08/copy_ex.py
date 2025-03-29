'''
파일명: copy_ex.py

얕은 복사와 깊은 복사
    - 두 복사의 차이는 객체(리스트, 딕셔너리 등)를 복사하는 방법의 차이다.
    - 중첩된 구조에서 복사하는 방법에 차이가 생긴다.
'''
import copy

origin_list = [1, [2, 3]]

copy_list = origin_list
copy_list[0] = 10
print(origin_list)
print(copy_list)

copy_list = origin_list.copy()
print(id(origin_list[1]), id(copy_list[1]))

copy_list[1][0] = 10
print(origin_list)
print(copy_list)

deepcopy_list = copy.deepcopy(origin_list)
deepcopy_list[1][0] = 20
print(origin_list)
print(deepcopy_list)
