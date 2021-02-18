"""
[지시사항]
1. Animal 클래스의 인스턴스 dog를 만들고 name에는 강아지, say에는 멍멍!을 저장해보세요.
2. saying 메서드를 이용해서 dog의 울음소리를 출력해보세요.
"""


class Animal():
    name = ''
    say = ''

    def saying(self):
        print(self.say)


dog = Animal()
dog.name = '강아지'
dog.say = '멍멍!'

dog.saying()
