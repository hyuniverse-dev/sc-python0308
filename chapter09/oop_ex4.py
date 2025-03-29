'''
파일명: oop_ex4.py

클래스 메소드
    - 클래스가 가지고 있는 메소드이다. 인스턴스 종속되지 않는다.
    - @classmethod 라는 데코레이터를 사용해야 한다.

데코레이터
    - 꾸며주는 기능이 있다.
'''

class Student:

    @classmethod
    def print_all(cls):
        print("클래스 메소드가 실행되었습니다.")

Student.print_all()