'''
파일명: function_ex2.py

사용자 함수
    - 사용자가 직접 만드는 함수이다.
    - 파이썬 내장함수로는 모든 문제를 해결할 수 없다.
    - 따라서 업무에 맞는 특정 기능을 구현한 함수가 필요하다.

용어 정리
    - 함수 정의
    - Arguments(인수 / 파라미터라는 용어도 혼재해서 사용한다.)
    - 파라미터(매개변수)
    - 반환값 / 리턴값
    - 함수 호출

함수의 종류
    - 파라미터 X / 리턴값 X
    - 파라미터 O / 리턴값 X
    - 파라미터 X / 리턴값 O
    - 파라미터 O / 리턴값 O
'''

# 전달받은 value를 n번만큼 반복해서 출력하는 함수
#   매개변수에 초기값을 설정하면 기본 매개변수로 사용되고, 파라미터를 넘겨주지 않아도 기본값이 적용된다.
def print_n_times(value, n = 2):
    for i in range(n):
        print(value)


print_n_times("Hello!", 5)
print_n_times("Bye!")
print_n_times("Welcome!", 10)

# 가변 매개변수 - 여러 개의 데이터를 유연하게 전달받을 수 있다.
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬", "수업입니다!")
