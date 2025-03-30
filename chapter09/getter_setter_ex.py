'''
파일명: getter_setter_ex.py

게터(getter)와 세터(setter)
    - 속성을 프라이빗 변수로 관리하면 안전하게 사용할 수 있다.
    - 하지만 속성에 접근하고 싶을 때 현재는 불가능하다.
    - 간접적으로 접근할 수 있는 방법을 만들어줘야 한다. 이게 게터와 세터이다.
'''
import math


class Circle:

    def __init__(self, radius):
        if (radius < 0):
            self.__radius = 0
        else:
            self.__radius = radius

    # 원의 둘레 구하는 메소드
    def get_circumference(self):
        return 2 * math.pi * self.__radius

    # 원의 넓이를 구하는 메소드
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # 게터
    #   클래스 내부에서는 프라이빗 변수에 접근이 가능하기 때문에
    #   대신 값을 반환해준다.
    def get_radius(self):
        return self.__radius

    # 세터
    #   클래스 내부에서는 프라이빗 변수에 접근이 가능하기 때문에
    #   대신 값을 대입해준다.
    def set_radius(self, radius):
        if radius < 0:
            self.__radius = 0
        else:
            self.__radius = radius


circle = Circle(10)
print(circle.get_radius())

circle.set_radius(20)
print(circle.get_radius())

circle2 = Circle(-20)
