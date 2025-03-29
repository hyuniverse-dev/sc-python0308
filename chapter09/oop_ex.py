'''
파일명: oop_ex.py

객체지향 프로그래밍
    - 객체를 중심으로 개발하는 방법론을 의미한다.
    - 고유한 속성(데이터)과 기능(함수)을 기반으로 객체를 생성하고,
      프로그램에서 사용한다.

객체
    - "특정 대상"이라는 의미로 이해한다.
    - 해당 객체만의 고유한 속성과 기능이 구성되어야 한다.
    - 현실 세계의 대상을 그대로 반영하진 않고,
      내 프로그램에 맞는 객체로 모델링하여 사용한다.
'''

def intro(students: list):
    for student in students:
        name = student.get("name")
        korean = student.get("korean")
        math = student.get("math")
        print(f"제 이름은 {name}이고, 국어점수: {korean}, 수학점수: {math} 입니다.")


students = [
    {"name": "옥순", "korean": 90, "math": 89},
    {"name": "영철", "korean": 60, "math": 55},
    {"name": "영식", "korean": 30, "math": 43}
]

intro(students)
