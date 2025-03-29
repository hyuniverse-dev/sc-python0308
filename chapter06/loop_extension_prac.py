'''
파일명: loop_extension_prac.py
'''

"""
다음 빈칸을 채워서 중첩 반복문을 
사용한 구구단 2단 ~ 9단, 출력 프로그램이 다음과 같이 출력되도록 완성하세요.

✅ <실행 결과>

2단
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18

… 

9단
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
"""


for first_number in range(2, 10):  # 외부 루프: 2단부터 9단까지 반복
    print(f"{first_number}단")
    for second_number in range(1, 10):  # 내부 루프: 1부터 9까지 반복
        result = first_number * second_number
        print(f"{first_number} x {second_number} = {result}")
    print()  # 각 구구단 출력 후 빈 줄 추가
