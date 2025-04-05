'''
파일명: file_io_prac2.py

금칙어 "*" 처리하기
    - 주어진 특정 단어들이 문자열에 포함된 경우 해당 단어만 "*" 로 처리한다.

- 요구 사항
1. 금지어.txt 라는 파일이 주어지며, 파일에는 여러 개의 문장이 포함되어 있습니다. 예를 들어 파일의 내용이 다음과 같다고 가정합니다.
오늘도 실수했어요. 저는 진짜 바보 같아요. 친구들 앞에서 멍청이처럼 행동했어요.

2. 프로그램은 filter_words 라는 리스트에 금지어를 포함하고 있어야 하며, 리스트의 단어가 파일에 등장할 경우 동일한 길이의 별표(*)로 치환해야 합니다.
예를 들어 filter_words = [”바보”, “멍청이”]일 경우, “바보”는 “**”로 “멍청이”는 “***”로 치환됩니다.

3. 파일을 읽어서 금지어를 치환한 결과를 출력하세요.

- 예시 출력
1. 금지어.txt 파일의 내용:
  오늘도 바보 같아요. 멍청이 같다고 느껴져요.

2. filter_words = [”바보”, “멍청이”]일 경우 프로그램 출력은 다음과 같아야 합니다.
  오늘도 ** 같아요. *** 같다고 느껴져요.
'''

# 파일 열기
with open('C:\sc-python0308-main\data\금칙어.txt', 'rt', encoding='utf-8') as file:
    # 금칙어 목록
    # filter_words = ['바보', '멍청이', '실수']

    # 사용자로부터 입력을 받은 단어를 별표 처리하기
    filter_words = []

    while True:
        user_input = input("금칙어를 입력하세요 >>> ")

        if not user_input:
            break

        filter_words.append(user_input)
    # 파일 내용 읽기
    content = file.read() # 텍스트 파일 안의 데이터를 하나의 문자열로 반환

    # 금칙어 필터링
    for item in filter_words:
        content = content.replace(item, '*' * len(item))

    # 필터링된 내용 출력
    print("필터링된 내용:")
    print(content)


##### replace() 예시
message = "안녕하세요."
message = message.replace("안녕하세요", "hello")
print(message)









