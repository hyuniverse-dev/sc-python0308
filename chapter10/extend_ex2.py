"""
파일명: extend_ex2.py
"""


# 부모 클래스
class Person:
    # 생성자
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 메소드
    def introduce(self):
        return f"안녕하세요. 제 이름은 {self.name}입니다. 저는 {self.age}살 입니다."

# 자식 클래스-1
class Student(Person):
    # 생성자
    def __init__(self, name, age, gender, korean, math, english):
        super().__init__(name, age, gender)
        self.korean = korean
        self.math = math
        self.english = english

    # 메소드
    def get_sum(self):
        return self.korean + self.math + self.english
    
    # 메소드 오버라이드
    def introduce(self):
        return f"{super().introduce()} - 저는 학생입니다."

# Teacher 자식 클래스 선언 - Person 클래스 상속

#   subject 멤버 필드를 추가

#   introduce() 메소드 오버라이딩
#   : super().introduce() - 저는 강사입니다. 담당 과목은 00입니다.


###########
student = Student("노아", 20, "남자", 100, 90, 100)
print(student.name, student.age, student.gender, student.korean, sep=" / ")
print(student.introduce())
print(student.get_sum())

# Teacher 인스턴스 생성
# introduce() 메소드 호출







