'''
[지시사항]
1. Human 클래스의 멤버 변수 __name과 __birthday를 매개변수로 받아 값을 수정하는 __set() 함수를 만드세요.
2. Human 클래스의 멤버 변수 __name을 반환하는 get_name() 함수를 만드세요.
3. Human 클래스의 멤버 변수 __birthday를 반환하는 get_birthday() 함수를 만드세요.
'''


class Human:
    def __init__(self, name, birthday):
        self.__set(name, birthday)

    def __set(self, __name, __birthday):
        self.name = __name
        self.birthday = __birthday

    def get_name(self):
        return self.name

    def get_birthday(self):
        return self.birthday


person = Human("홍길동", 990101)
person.get_name()
person.get_birthday()