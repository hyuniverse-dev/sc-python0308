'''
파일명: input_function2.py
'''

x = int(input("첫 번째 숫자를 입력하세요 >>> "))
y = int(input("두 번째 숫자를 입력하세요 >>> "))

# 두 정수를 합한 결과를 출력
print(x + y)

# input() 함수는 기본 반환 타입이 문자열이기 때문에 "문맥적 오류"가 발생한다.
# 따라서 자료형변환(type casting)을 사용해야 한다.