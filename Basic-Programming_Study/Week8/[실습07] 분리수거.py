"""
[지시사항]
1. recycle 모듈을 불러오세요.
2. Recycle 클래스의 객체로 coke_can 인스턴스를 만들고 다음 메서드를 호출해보세요.
    canRecycle()
    whatTrash('can')
    throwTrash()
3. Recycle 클래스의 객체로 clothes 인스턴스를 만들고 다음 메서드를 호출해보세요.
    whatTrash('cloth')
    throwTrash()
"""

from recycle import Recycle

coke_can = Recycle()

coke_can.canRecycle()
coke_can.whatTrash('can')
coke_can.throwTrash()

clothes = Recycle()

clothes.whatTrash('cloth')
clothes.throwTrash()
