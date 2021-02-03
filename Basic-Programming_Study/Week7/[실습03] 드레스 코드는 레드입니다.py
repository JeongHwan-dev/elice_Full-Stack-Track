"""
[지시사항]
1. end가 입력될 때까지 입력을 받아 dress_code 리스트에 입력한 뒤 출력하세요.
2. dress_code 리스트에서 red를 모두 제거하고 출력하세요.
"""

# 친구들의 드레스 코드를 담을 리스트입니다.
dress_code = list()

# 1번을 하세요.
while True:
    dress = input()
    if dress == 'end':
        break
    else:
        dress_code.append(dress)

# 입력을 잘 받았는지 확인하는 코드입니다.
print(dress_code)

# 2번을 하세요.
dress_code = list(filter(('red').__ne__, dress_code))

# red 옷을 입은 사람이 제외되었는지 확인하는 코드입니다.
print(dress_code)
