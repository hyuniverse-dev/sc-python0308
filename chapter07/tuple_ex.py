'''
파일명: tuple_ex.py

튜플
    - 리스트와 비슷한 자료구조이다.
    - 읽기 전용이기 때문에 데이터가 한번 생성되면 수정이 불가능하다.
    - 패킹/언패킹을 사용할 수 있는 자료구조이다.
    - 리스트는 [] 였지만, 튜플은 () 로 그룹화 한다.
    - 함수에서 데이터를 반환값에 나열해서 반환하면 자동으로 튜플로 패킹되는 것이 대표적인 예이다.
'''

tuple_a = (1, 2, 3, 4, 5)
print(tuple_a)

# 패킹 - 여러 값을 하나의 튜플로 묶는 과정을 의미한다.
#     - 하나의 변수(식별자)에 여러 개의 데이터를 할당하면 자동으로 튜플로 패킹
tuple_a = 5, 4, 3, 2, 1
print(tuple_a)

# 언패킹 - 튜플 안의 값을 개별 변수로 추출하는 작업이다.
a, b, c, d, e = tuple_a
print(a)
print(b)
print(c)
print(d)
print(e)

# 리스트와 튜플을 활용하여 그룹화하기
users = [(1, "노아"), (2, "소닉"), (3, "이슬라")]
users.append((4, "미아"))
for user in users:
    user_number, user_name = user
    print(f"회원아이디: {user_number}, 회원이름: {user_name}")


tuple_a = (1, 2, 3, 4, 5)
print(list(tuple_a)) # 튜플을 list로 타입 캐스팅하고, 리스트 관련 함수 사용


# 튜플의 다양한 함수들
#   - 튜플은 수정이 불가능한 객체(immutable 객체)이기 때문에 파괴적인 함수는 사용 불가능하다.
#   - len(), .index(), max(), min(), sum() 과 같이 반환값이 존재하는 함수들은 대체로 사용 가능하다.
tuple_a = 1, 2, 3, 4, 5
list_a = sorted(tuple_a, reverse=True)
print(tuple(list_a))
print(tuple_a)

print(len(tuple_a))
print(tuple_a.index(1))
print(max(tuple_a))
print(min(tuple_a))
print(sum(tuple_a))


