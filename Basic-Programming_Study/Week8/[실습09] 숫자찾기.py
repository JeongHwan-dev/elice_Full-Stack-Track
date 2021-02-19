"""
[지시사항]
1. 리스트를 매개변수로 받고 해당 리스트 안에 필드 num 이 있으면 True 없으면 False 를 반환하는 find() 메서드를 완성해보세요.
2. 필드 num 을 매개변수 n으로 설정하는 setNum() 메서드를 완성해보세요.
"""


class findNumber():
    num = 0

    def find(self, num_list):
        return self.num in num_list

    def setNum(self, n):
        self.num = n

