'''
파일명: oop_prac2.py
'''
from tkinter.font import names


class Student:
    # 클래스 변수
    student_count = 0
    students = []
    students_name = []

    # 생성자 함수
    def __init__(self, name, korean, math, english):
        # name, korean, math, english 멤버 필드 선언
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        
        # 카운트 증가
        Student.student_count += 1


        # students 리스트에 인스턴스 추가
        Student.students.append(self)


    # 클래스 메소드 정의
    #   print_all()
    @classmethod
    def print_all(cls):
        print(cls.students)
        print("=== 학생 목록 ===")
        print(f"이름     총점     평균")
        for student in cls.students:
            print(f"{student.name}     {student.get_sum()}     {student.get_average()}") # 수정 예정
        print("================")

    # 인스턴스 메소드 정의
    #   get_sum(), get_average()
    def get_sum(self):
        return self.korean + self.math + self.english

    def get_average(self):
        return self.get_sum() / 3


noah = Student("Noah", 100, 90, 80)
Student.print_all()
# 노아의 총점과 평균을 가져온다.
print(noah.get_sum())
print(noah.get_average())

mia = Student("Mia", 100, 100, 100)
Student.print_all()
