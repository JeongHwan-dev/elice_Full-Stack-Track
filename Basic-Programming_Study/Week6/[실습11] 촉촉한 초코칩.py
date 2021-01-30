"""
[지시사항]
1. 임의의 길이에 문자열을 입력받으세요.
2. 직접 입력받은 문자열에 있는 촉촉한 초코칩의 횟수만 출력해 주세요.
"""

s = input()

chocochip = '촉촉한 초코칩'
choco_count = 0

for i in range(len(s) - 6):
    if s[i] == '촉' and s[i + 1] == '촉' and s[i + 2] == '한' and s[i + 3] == ' ' and s[i + 4] == '초' and s[i + 5] == '코' and s[i + 6] == '칩':
        choco_count += 1

print(choco_count)
