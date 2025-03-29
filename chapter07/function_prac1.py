'''
파일명: function_prac1.py
'''

"""
문제
빈칸을 채워서 다음 두 개의 정수를 매개변수로 사용하는 
sum_all() 함수를 정의하고, 입력받은 두 개 정수 범위의 모든 정수를 더하는 함수를 완성하세요.
"""


def sum_all(start: int, end: int):  # sum_all 함수 정의
    output = 0  # 초기값 설정
    for i in range(start, end + 1):  # start부터 end까지 반복
        output += i  # output에 i를 더함
    return output  # 결과 반환


print("0 to 100:", sum_all(0, 100))  # 0부터 100까지 더한 값 출력
print("0 to 1000:", sum_all(0, 1000))  # 0부터 1000까지 더한 값 출력
print("50 to 100:", sum_all(50, 100))  # 50부터 100까지 더한 값 출력
print("500 to 1000:", sum_all(500, 1000))  # 500부터 1000까지 더한 값 출력
