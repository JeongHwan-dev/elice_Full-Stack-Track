"""
[입력 예시]
300

[출력 예시]
1 1 1
"""

g = int(input())

if g % 10 == 0:
    protein_cube = g // 250
    g = g % 250
    chicken_cube = g // 40
    g = g % 40
    peanut_cube = g // 10

    print(peanut_cube, chicken_cube, protein_cube)

else:
    print(-1)
