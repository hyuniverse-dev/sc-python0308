'''
파일명: isinstance.py

isinstance() 함수
    - 상속 관계를 고려한다.
    - 따라서 type() 함수로 인스턴스 체크하는 것과 차이가 있다.
'''

class Parent:
    def __init__(self):
        self.value = "Parent"

    def introduce(self):
        print("안녕하세요.")

class Child(Parent):
    def __init__(self):
        super().__init__()

class Child2(Parent):
    def __init__(self):
        super().__init__()

class Student():
    def __init__(self):
        self.value = "Student"

parent = Parent()
child = Child()
child2 = Child2()
student = Student()

# type() 함수로 인스턴스 검사하기
print(type(student) == Parent)

# isinstance() 함수로 검사하기
print(isinstance(child, Parent))
print(isinstance(child2, Parent))

# isinstance() 활용하기
items = [parent, child, child2, student]

for item in items:
    # 상속관계를 고려한 인스턴스 검사 후에 메소드 실행
    if isinstance(item, Parent):
        item.introduce()