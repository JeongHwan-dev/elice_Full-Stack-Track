"""
[지시사항]
1. True 가 주어지면 False 를, False 가 주어지면 True 를 반환하는 함수 tree_frog 를 완성하세요.
"""


# 1번을 해보세요.
def tree_frog(boolean):
    if boolean is True:
        return False
    else:
        return True


# 값이 잘 나오는지 테스트 해보세요!
print(tree_frog(1 == 1))
