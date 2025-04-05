'''
파일명: file_io_ex2.py
'''

# write 모드
file = open("hello.txt", "wt", encoding="utf-8")

file.write("hello")
file.write("\n")
file.write("world!")

print("hello.txt 파일이 생성되었습니다.")

file.close()

# data 디렉토리에 hello.txt 파일을 생성하세요. (상대경로 사용)
file = open("../data/hello.txt", "wt", encoding="utf-8")
file.write("hello")
file.write("\n")
file.write("world!")

print("hello.txt 파일이 생성되었습니다.")

file.close()

# data 디렉토리에 hello2.txt 파일을 생성하세요. (절대경로 사용)
file = open("C:/sc-python0308-main/data/hello2.txt", "wt", encoding="utf-8")

file.write("hello")
file.write("\n")
file.write("world!")

print("hello.txt 파일이 생성되었습니다.")

file.close()

# 쓰기 모드 주의사항
#   파일이 존재할 때 덮어쓴다.
file = open("hello.txt", "wt", encoding="utf-8")

file.write("bye")
file.write("\n")
file.write("world!")

print("hello.txt 파일이 생성되었습니다.")

file.close()





