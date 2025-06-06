'''
파일명: function_prac2.py
'''

"""
다음 빈칸을 채워서 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수를 완성하세요.
"""

def mul(*values): # 가변 매개변수를 사용해서 mul() 함수를 정의
    output = 1 # 초기값 설정
    for value in values: # 반복문을 통해 모든 매개변수를 순회
        output *= value # 변수에 누적하여 곱한 값을 저장 (output = output * value)
    return output # 결과 반환

res = mul(5, 7, 9, 10, 11, 12, 13)
print(res)  # 3150  
