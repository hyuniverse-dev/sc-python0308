'''
파일명: oop_prac.py

Teacher 클래스를 정의
    - 속성: name, age, subject
'''


class Teacher:

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    # introduce() 메소드를 정의한다.
    #   "안녕하세요. 저는 00 과목을 맡고 있는 00 강사입니다! 나이는 00 살 입니다." 출력
    def introduce(self):
        print(f"안녕하세요. 저는 {self.subject}과목을 맡고 있는 {self.name} 강사입니다! 나이는 {self.age} 살 입니다.")


# Teacher 인스턴스 생성후 출력하여 참조주소 확인
noah = Teacher("Noah", 20, "Python")
print(noah)

# Teacher 인스턴스의 name, age, subject 출력하기

print(noah.name)
print(noah.age)
print(noah.subject)

# Teacher 인스턴스의 name 수정하기
noah.name = "노아"
print(noah.name)

# introduce() 메소드 호출
noah.introduce()
