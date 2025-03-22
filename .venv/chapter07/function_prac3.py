'''
파일명: function_prac3.py
'''

"""
빈칸을 채워서 사용자로부터 입력받은 여러 개의 정수 중 
최대값과 최소값을 동시에 출력하는 프로그램을 완성하세요.

(기획)
    사용자로부터 입력받은 모든 숫자들의 최대값과 최소값 구하기

(조건)
		1. 사용자는 최소 2개 이상의 정수를 제한없이 프로그램이 실행되는 동안 무한히 입력할 수 있습니다.
		2. 사용자가 0을 입력하면 입력을 종료합니다.
		3. 입력받은 숫자는 리스트로 관리합니다.
		4. find_max_min_value 함수를 정의하고 사용자가 입력한 숫자 리스트를 매개변수로 받아
       함수 내에서 구한 최대값과 최소값을 호출자에게 반환합니다.
		5. 호출자는 반환받은 데이터를 다음 표준출력과 동일하게 출력합니다.


(표준입력)
		(테스트 케이스1)
		1번째 정수를 입력하세요.(종료는 0을 입력하세요.) >>> 
		2번째 정수를 입력하세요.(종료는 0을 입력하세요.) >>> 
		...
		n번재 숫자를 입력하세요. (종료는 0을 입력하세요.) >>> 

		(테스트 케이스2)
		1번째 숫자를 입력하세요. (종료는 0을 입력하세요.) >>> 123
		2번째 숫자를 입력하세요. (종료는 0을 입력하세요.) >>> 0

(표준출력)
		(테스트 케이스1)
		최대값: 113, 최소값: 1

		(테스트 케이스2)
		최소 2개 이상의 숫자를 입력하세요.
"""


# 함수 정의 - 여러 개의 정수를 제공하고, 최대값과 최소값을 구해서 반환시킨다.
def find_max_min_value(numbers: list):
    """
    주어진 숫자 리스트에서 최대값과 최소값을 찾아서 반환하는 함수이다.

    :param numbers: 숫자 리스트
    :return: 최대값과 최소값
    """

    ##### 기본 방식
    # max_value = numbers[0]  # 최대값을 담을 변수
    # min_value = numbers[0]  # 최소값을 담을 변수

    # 반복문을 사용해서 현재 가져온 요소가 max_value보다 크면 max_value 에 대입
    # 반복문을 사용해서 현재 가져온 요소가 min_value보다 작으면 min_value 에 대입
    # for number in numbers:
    #     if number > max_value:
    #         max_value = number
    #
    #     if number < min_value:
    #         min_value = number

    ##### max(), min() 함수 사용
    max_value = max(numbers)
    min_value = min(numbers)

    # 결과값을 반환
    return max_value, min_value # [max_value, min_value] 리스트 반환


# 사용자로부터 입력받을 받는 무한루프
numbers = []
# count = 0
while True:
    number = int(input("정수를 입력해주세요. (종료는 0을 입력) >>> "))

    # 입력을 받은 데이터가 0이면 탈출
    # 입력을 받은 데이터가 0이 아니면 리스트에 데이터 추가
    # 입력받은 데이터가 총 2개 미만이면
    if number != 0:
        numbers.append(number)
    else:
        if len(numbers) < 2:
            print("최소 2개 이상의 숫자를 입력하세요.")
        else:
            break

# 최대/최소값 구하는 find_max_min_value() 호출해서 결과 반환
max_value, min_value = find_max_min_value(numbers)

# 결과를 반환받고 출력
print(f"최대값: {max_value}, 최소값: {min_value}")