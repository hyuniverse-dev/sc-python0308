'''
파일명: extend_ex.py

상속
    - 부모 클래스가 자식 클래스에서 속성과 기능을 물려주는 것을 의미한다.
    - 부모 클래스는 슈퍼 클래스라고 하고, 자식 클래스는 서브 클래스라고 한다.
    - 파이썬에서는 다중 상속이 가능은 하지만 코드의 복잡성이 높아지기 때문에
      자식 클래스는 하나의 부모 클래스를 상속하는 구조로 만든다.
    - 상속하는 방법은 클래스명 뒤에 () 소괄호를 사용해서 상속받을 클래스명을 기술한다.
'''

class Parent:
    # 부모 클래스 생성자
    def __init__(self):
        self.value = "Parent"
        print("부모 클래스 생성자가 호출되었습니다.")

    # 부모 클래스 메소드
    def test_method(self):
        print("부모 클래스 메소드가 호출되었습니다.")

class Child(Parent):
    # 자식 클래스 생성자
    def __init__(self):
        # 부모 생성자 호출
        super().__init__()
        print("자식 클래스 생성자가 호출되었습니다.")


# 자식 클래스를 통해서 인스턴스 생성
child = Child()
res = child.value
print(res)

child.test_method()