'''
파일명: lotto_service.py
'''

import random
from chapter98.application.email_service import send_email


def store_numbers():
    numbers = set()

    while len(numbers) < 6:
        number = random.randint(1, 45)
        numbers.add(number)

    numbers = list(numbers)

    return f"""
    [ 이번 주 당첨 번호를 알려드릴게요 :) ]
    1번 번호: {numbers[0]}
    2번 번호: {numbers[1]}
    3번 번호: {numbers[2]}
    4번 번호: {numbers[3]}
    5번 번호: {numbers[4]}
    6번 번호: {numbers[5]}
    """

if __name__ == "__main__":
    numbers = store_numbers()
    send_email("hyuniverse.dev@gmail.com", "오늘의 행운의 번호", numbers)

