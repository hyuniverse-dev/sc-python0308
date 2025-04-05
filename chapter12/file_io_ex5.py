'''
파일명: file_io_ex5.py

파일 읽기
    - read 모드
    - read(), readline(), readlines()
'''
from idlelib.iomenu import encoding

# read()
#   - read() 메소드에 파라미터로 정수값을 넘겨주면 해당 크기만큼만 읽어온다.
#   - read() 메소드에 파라미터로 아무값도 넘겨주지 않으면 전체를 읽어온다.
print("##### read()")
file = open("2025-04-05.txt", "rt", encoding="utf-8")

content = file.read()
print(content)

print("파일을 읽어왔습니다.")
file.close()

print("##### readline()")
# readline()
#   - 한 줄씩 읽어서 처리
file = open("2025-04-05.txt", "rt", encoding="utf-8")

while True:
    content = file.readline()

    if not content:
        break

    print(content, end="")

print("파일을 읽어왔습니다.")
file.close()

# readlines()
#   - 한 줄을 하나의 요소로 반환해서 처리
print("##### readlines()")
file = open("2025-04-05.txt", "rt", encoding="utf-8")

content = file.readlines()

for word in content:
    print(word, end="")

print("파일을 읽어왔습니다.")
file.close()
