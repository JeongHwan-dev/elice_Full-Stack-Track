"""
[지시사항]
1. math 모듈을 불러오세요.
2. 구의 부피 공식을 이용해 지구의 부피를 계산하고 volume 변수에 저장하세요. 반지름에는 6371을 넣고 파이값은 math 모듈에 있는 pi를 이용하세요.
"""

import math

radius = 6371                                       # 지구의 반지름
volume = (4/3) * math.pi * math.pow(radius, 3)      # 지구의 부피

print(volume)