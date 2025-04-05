'''
파일명: file_io_ex6.py

with 문
    - 프로그램이나 파일의 에러로 인해서 close() 메소드가 호출되지 않는 문제를 방지할 수 있는 구문
'''

# file = open("lyrics.txt", "rt", encoding="utf-8") + file.close() 를 아래 with 문으로 대체 할 수 있다.

with open("lyrics.txt", "rt", encoding="utf-8") as file:
    lyrics = file.readlines()
    for item in lyrics:
        print(item, end="")