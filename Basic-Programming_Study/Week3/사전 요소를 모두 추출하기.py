# 실습에 사용할 변수를 선언합니다.
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
solardict = {'태양':'Sun', '지구':'Earth', '달':'Moon'}

# 1. names의 모든 요소를 추출하여 변수 items1에 저장하세요.
items1 = names.items()

# 2. items1에 객체형으로 저장된 names의 모든 요소를 리스트형으로 변경한 후 변수 item_list1에 저장하세요.
item_list1 = list(items1)

# 3. solardict의 모든 요소를 추출하여 변수 items2에 저장하세요.
items2 = solardict.items()

# 4. items2에 객체형으로 저장된 solardict의 모든 요소를 리스트형으로 변경한 후 변수 item_list2에 저장하세요.
item_list2 = list(items2)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('names의 모든 요소를 객체형으로 추출합니다:\n>>>', items1)
print('names의 모든 요소를 리스트에 담습니다:\n>>>', item_list1)
print('solardict의 모든 요소를 객체형으로 추출합니다:\n>>>', items2)
print('solardict의 모든 요소를 리스트에 담습니다:\n>>>', item_list2)