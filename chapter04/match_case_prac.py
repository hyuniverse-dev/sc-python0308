'''
파일명: match_case_prac.py
'''

"""
연습문제

사용자로부터 과일 이름을 입력받고
다음 출력문을 출력하세요.
"""

# 데이터 입력받기(메세지: Enter a fruit >>> )
input_fruit = input("Enter a fruit >>> ")

# match-case 문으로 출력문 분기하기
match input_fruit.lower():
    case "apple":
        print("Apple is red")
    case "banana":
        print("Banana is yellow")
    case "cherry":
        print("Cherry is red")
    case _:
        print("Unknown fruit")
