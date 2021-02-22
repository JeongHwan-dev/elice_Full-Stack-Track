"""
[지시사항]
1. 클래스 내 메소드(eat())의 위로 한 번의 줄바꿈을 하세요.
2. 클래스(Bread)의 정의가 끝나는 곳에 두 번의 줄바꿈을 하세요.
3. 인스턴스 선언, 인스턴스 변수 대입, 클래스 메서드 호출끼리는 묶고 그사이를 한 번의 줄바꿈으로 구분하세요.
"""


class Bread():
    taste = "밀가루"

    def eat(self):
        print(self.taste, "맛이 나요!")


redBean = Bread()  # 인스턴스 선언
choux = Bread()

redBean.taste = "팥"  # 인스턴스 변수 대입
choux.taste = "슈크림"

redBean.eat()  # 클래스 메서드 호출
choux.eat()
