'''
파일명: function4_ex.py

함수 모듈화
    - 코드를 최대한 작은 단위의 독립적인 함수로 분할하여 조직화 하는 방법이다.
    - 유지 보수를 쉽게 만들어주기 위해서 사용하는 방법이다.

함수 모듈화 전략(strategy)
    - 작은 단위 기준으로 함수를 구성해야 한다.
    - 각 함수는 단위별로 재사용이 가능해야 한다.
    - 가급적 특정 로직에 종속되지 않도록 구성한다.
'''


def find_max_min_value(numbers: list):
    """
    정수 리스트를 받아서 최대/최소 값을 반환하는 함수이다.

    :param numbers: 정수 리스트
    :return: 최대/최소 값
    """
    return max(numbers), min(numbers)


# 테스트 코드 작성시 사용하는 조건문이다.
if __name__ == "__main__":
    numbers = [10, 20, 30]
    max_value, min_value = find_max_min_value(numbers)
    print(max_value, min_value)








