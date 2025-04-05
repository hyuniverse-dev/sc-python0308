'''
파일명: file_io_prac.py

뮤지컬 <모차르트!> 의 OST "황금별" 의 가사에서
"별" 과 "왕" 이라는 단어의 개수 세기
'''

# 파일 열기 (경로와 모드 설정)
file = open("lyrics.txt", "rt", encoding="utf-8")

# 파일 읽기 - readlines()
king_count = 0
star_count = 0
lyrics = file.readlines()

##### 사용자로부터 여러 개의 단어를 입력받고 검색할 때
# user_input = input("찾을 단어를 입력하세요 >>> ").split(",")
# user_input_1 = user_input[0]
# user_input_2 = user_input[1]

# "별" / "왕" 이라는 단어가 포함되어 있는지 카운트
for item in lyrics:
    if "별" in item:
        star_count += 1
    if "왕" in item:
        king_count += 1
    ###### 한 글자씩 비교할 때
    # for character in item:
    #     if "별" == character:
    #         star_count += 1
    #     elif "왕" == character:
    #         king_count

# 결과 출력
print(f"왕 == {king_count}번, 별 == {star_count}번 포함되어 있습니다.")

file.close()
