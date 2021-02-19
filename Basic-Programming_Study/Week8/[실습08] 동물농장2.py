"""
[지시사항]
1. Animal 클래스를 상속받는 Cat 클래스를 만들어 보세요.
2. 야옹을 출력하는 saying() 함수를 만들어 보세요.
3. Cat 클래스의 인스턴스 persian 을 만들고 saying() 함수를 호출해보세요.
"""


class Animal():
    def saying(self):
        print("--")


class Cat(Animal):
    def saying(self):
        print('야옹')


persian = Cat()
persian.saying()
