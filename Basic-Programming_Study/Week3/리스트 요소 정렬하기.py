# 실습에 사용할 변수를 선언합니다.
lotto770 = [34, 1, 43, 9, 12, 39, 23]
namelist = ['Marry', 'Sams', 'Aimy', 'Tom', 'Michael', 'Bob', 'Kelly']

# 1. sort를 이용해 lotto770의 원소를 오름차순으로 정렬하세요.
lotto770.sort()

# 2. sorted를 이용해 namelist의 원소를 알파벳 내림차순으로 정렬한 값을 ret에 저장하세요.
ret = sorted(namelist, reverse=True)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(lotto770)
print(ret)
