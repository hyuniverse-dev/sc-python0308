'''
파일명: exception_prac.py
'''

"""
✅ 다음 코드의 빈칸을 ①조건문을 사용한 코드와 ②try-except 구문을 사용한 코드로 채워서 예외가 발생하지 않고 
코드가 실행 결과처럼 출력되도록 만들어주세요.

< 실행결과 >
# (1) 요소 내부에 있는 값 찾기

- 52는 0 위치에 있습니다.

# (2) 요소 내부에 있는 값 확인(조건문을 사용한 코드)

- 52는 리스트 0에 존재합니다.

# (3) 요소 내부에 없는 값 찾기(try except 구문을 사용한 코드)

- 리스트 내부에 10000를 찾을 수 없습니다.

-- 정상적으로 종료되었습니다. ---
"""


numbers = [52, 273, 32, 103, 90, 10, 275]

print("# (1) 요소 내부에 있는 값 찾기")
print(f"- 52는 {numbers.index(52)} 위치에 있습니다.")
print()

print("# (2) 요소 내부에 있는 값 확인(조건문을 사용한 코드)")
number = 52
if number in numbers:
  print(f"- {number}는 리스트 {numbers.index(number)}에 존재합니다.")
else:
  print(f"- {number}는 리스트 내부에 존재하지 않습니다.")
print()

print("# (3) 요소 내부에 없는 값 찾기(try except 구문을 사용한 코드)")
number = 10000
try:
  print(f"- {number}는 {numbers.index(number)} 위치에 있습니다.")
except:
  print(f"- 리스트 내부에 {number}를 찾을 수 없습니다.")
print()



print("--- 정상적으로 종료되었습니다. ---")

