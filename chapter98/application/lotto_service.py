'''
파일명: lotto_service.py
'''

import random
from chapter98.application.email_service import *


def store_numbers():
    numbers = set()

    while len(numbers) < 6:
        number = random.randint(1, 45)
        numbers.add(number)

    numbers = list(numbers)

    return numbers

if __name__ == "__main__":
    numbers = store_numbers()
    template = get_template(numbers, "2025-04-13")
    send_email("hyuniverse.dev@gmail.com", "오늘의 행운의 번호", template)

