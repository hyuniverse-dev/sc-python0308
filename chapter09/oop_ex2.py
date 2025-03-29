'''
파일명: oop_ex2.py

클래스
    - 클래스는 객체를 효율적으로 생성하기 위한 구조이다.
    - 특정 객체의 속성과 기능을 정의하는 용도로 사용한다.
    - "설계도" 라는 개념을 적용한다.
'''


# 클래스명은 파스칼 케이스로 작성한다.
class Student:

    # 생성자 함수
    #   - 클래스를 통해서 인스턴스를 생성할 때 자동으로 호출되는 특별한 함수이다.
    #   - 인스턴스를 생성할 때 초기값을 대입시킨다.
    #   - 첫 번째 매개변수는 반드시 self 를 입력해야 한다. self 가 예약된 키워드는 아니기 때문에 다른 식별자를 사용해도 무관하다.
    #     하지만 "관례적"으로는 self 를 사용한다.
    #   - self 는 인스턴스 "자기 자신"을 의미한다.
    def __init__(self, name, korean, math, age):
        # 일반 함수처럼 특별한 로직 처리도 할 수 있다.
        # if korean < 50:
        #     print("보충학습 대상입니다.")
        # name, korean, math 가 해당 인스턴스의 변수: 인스턴스 변수(멤버 필드)
        self.name = name
        self.korean = korean
        self.math = math
        self.age = age

    # 학생 자기소개 메소드(method)
    #   클래스가 가지고 있는 함수를 메소드라고 한다.
    #   첫 번째 매개변수로 self 식별자를 사용한다.
    #   인스턴스 함수 혹은 멤버 함수라고도 한다.
    #   멤버 필드에 저장되어 있는 데이터를 직접 참조하여 사용할 수 있다. 매개값을 전달하지 않아도 기능이 동작한다.
    def intro(self):
        print(f"제 이름은 {self.name}이고, 국어점수: {self.korean}, 수학점수: {self.math} 입니다.")

    # 소멸자
    #   - 더 이상 해당 인스턴스가 사용되지 않으면 가비지 컬렉터가 소멸자 호출한다.
    #   - 메모리에서 해당 인스턴스를 제거한다.
    #   - 대표적으로 "더 이상 사용하지 않는 인스턴스" 라는 것은 식별자에 대입하지 않는 경우를 의미한다.
    def __del__(self):
        print(f"{self.name} 제거되었습니다.")


Student("영자", 100, 100, 20)


oksoon = Student("옥순", 100, 90, 20)
oksoon.intro()
print(oksoon)

print(oksoon.name)
print(oksoon.korean)
print(oksoon.math)


youngchul = Student("영철", 40, 40, 21)
youngchul.intro()
print(youngchul)






