# 1번을 해보세요.
list = input().split()


# 2번을 해보세요.
if '치즈' in list:
    if '달걀' in list:
        print(True)
    else:
        print(False)
elif '고구마' in list:
    if '김치' in list:
        print(True)
    else:
        print(False)
elif '감자' in list:
    if '토마토' in list:
        print(True)
    else:
        print(False)
else:
    print(False)