# MyClass 선언
class MyClass:
    # '안녕하세요'를 출력하는 클래스 메소드 `sayHello`를 선언하세요.
    def sayHello(self):
        print('안녕하세요')

    # name을 입력받아 print('%s! 다음에 보자' %name)을 실행하는 클래스 메소드 `sayBye`를 선언하세요.
    def sayBye(self, name):
        print('%s! 다음에 보자' %name)


# 아래는 출력을 위한 코드 입니다. 수정하실 필요 없습니다.
obj = MyClass()
obj.sayHello()  # '안녕하세요' 출력
obj.sayBye('철수')    # '철수! 다음에 보자' 출력