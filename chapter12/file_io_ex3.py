'''
파일명: file_io_ex3.py

추가 모드
    - append 모드를 사용하면 기존 파일 데이터 + 새로운 데이터를 추가한다.
'''

file = open("hello.txt", "at", encoding="utf-8")

file.write("Hello")
file.write("\n")
file.write("World!")

print("hello.txt 파일이 수정되었습니다.")

file.close()

# 상대 경로를 사용해서 data/hello.txt 파일에 데이터를 추가해보세요.
# 추가할 데이터 "bye" "world!"

# 절대 경로를 사용해서 data/hello2.txt 파일에 데이터를 추가해보세요.
# 추가할 데이터 "bye" "world!"













