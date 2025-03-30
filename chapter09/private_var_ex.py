'''
파일명: private_var_ex.py

프라이빗 변수
    - 외부로부터 멤버 필드에 직접 접근하지 못하도록 막는다.

캡슐화
    - 객체 내부의 모든 속성과 기능에 접근하지 못하도록 만드는 것을 캡슐화라고 한다.
'''

import math


# 클래스 선언
class Circle:

    def __init__(self, radius):
        self.__radius = radius  # 프라이빗 변수: 변수명 앞에 __ 붙여준다. (외부에서 접근이 안된다.)

    # 원의 둘레 구하는 메소드
    def get_circumference(self):
        return 2 * math.pi * self.__radius

    # 원의 넓이를 구하는 메소드
    def get_area(self):
        return math.pi * (self.__radius ** 2)


circle = Circle(10)  # 최초 대입된 반지름의 값인 10이 고정된다.
print(circle.get_circumference())
print(circle.get_area())
