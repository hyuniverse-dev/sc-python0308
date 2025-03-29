'''
파일명: oop_ex3.py

클래스 변수
    - 인스턴스에 종속되어 있지 않고, 클래스를 통해서 직접 접근 가능하다.
    - 클래스 변수는 모든 인스턴스에 공유된다.
'''


class Student:
    # 클래스 변수
    class_var = 0
    student_count = 0

    # 인스턴스 변수(멤버 필드)
    def __init__(self, name):
        self.name = name
        Student.student_count += 1


res = Student.class_var
print(res)

noah = Student("노아")
print(Student.student_count)

sonic = Student("소닉")
print(Student.student_count)

mia = Student("미아")
print(Student.student_count)
