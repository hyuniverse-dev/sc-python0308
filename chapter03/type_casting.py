'''
파일명: type_casting.py

자료형변환
    - 데이터를 내가 원하는 자료의 형태로 변환해준다.
'''

# 타입 확인하기
number_value = 1
string_value = "문자열"
float_value = 3.14
bool_value = True

print(type(number_value))
print(type(string_value))
print(type(float_value))
print(type(bool_value))

# 데이터를 정수로 변환하기
string_value = "10"
int_value = int(string_value)
print(type(int_value))

# 데이터를 문자열로 변환하기
string_value2 = str(int_value)
print(type(string_value2))

# 데이터를 실수로 변환하기
float_value = float(string_value)
print(type(float_value))

# 변환이 불가능한 데이터
# int("abc") -> ValueError 발생! 숫자 데이터로 변환이 불가능한 데이터는 오류가 발생한다.




