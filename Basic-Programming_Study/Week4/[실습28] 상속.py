'''
[지시사항]
1. FindSix 클래스의 생성자에 FindTen의 __init__() 함수에 아래 코드를 추가하세요.
    self.find_five = FindTen(number)

2. 변수명 FindSix 클래스에서 self.find_five.five()를 return 하는 새로운 five() 함수를 만드세요.
'''


class FindTen:
    def __init__(self, number):
        self.number = number

    def two(self):
        return self.number % 2

    def five(self):
        return self.number % 5


class FindSix:
    def __init__(self, number):
        self.number = number
        self.find_five = FindTen(number)

    def two(self):
        return self.number % 2

    def three(self):
        return self.number % 3

    def five(self):
        return self.find_five.five()
