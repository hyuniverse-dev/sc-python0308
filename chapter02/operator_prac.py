'''
파일명: operator_prac.py

연산자 실습문제
'''

'''
다음 (?)을 채워 두 자리 정수 45를 십의 자리와 일의 자리로 분리하여 
출력하는 프로그램을 구현하세요.

# 문제
# number 변수를 선언하고 초기화 합니다.
number = 45

# 십의 자리와 일의 자리를 계산합니다.
tens = (?)  # 십의 자리를 구합니다.
units = (?)  # 일의 자리를 구합니다.

# 결과를 출력합니다.
print("십의 자리:", tens)
print("일의 자리:", units)
'''

number = 45

tens = number // 10
units = number % 10

print("십의 자리: ", tens)
print("일의 자리: ", units)

'''
1분은 60초이고, 1시간은 60분입니다 따라서 1시간은 3600초입니다.
3690 초를 시, 분, 초로 변환하여 출력하는 프로그램을 구현하세요.
'''

# total_seconds을 선언하고 초기화 합니다.
total_seconds = 3690

# 시간, 분, 초를 계산합니다.
hours = total_seconds // 3600  # 시간을 구합니다.
left_seconds = total_seconds % 3600  # 시간을 제외한 나머지 초를 구합니다.
minutes = left_seconds // 60  # 분을 구합니다.
seconds = left_seconds % 60  # 초를 구합니다.

# 결과를 출력합니다.
print("시:", hours)
print("분:", minutes)
print("초:", seconds)

print(hours, "시간 ", minutes, "분 ", seconds, "초")

# f-strings(문자열 포맷팅) - 변수를 문자열 내부에서 사용할 수 있도록 한다.
# 파이썬 3.6 버전 이상부터만 사용 가능하다.
print(f"{hours}시간 {minutes}분 {seconds}초")
