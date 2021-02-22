"""
[지시사항]
1. korean, chinese, western 변수에 가격을 넣어주세요.
2. discount_korean 변수에 할인된 한식의 가격을 저장하세요.
3. total_price 변수에 모든 학생이 고른 메뉴에 대한 전체 예산을 계산하여 저장하세요.
"""

# 한식 가격
korean = 7000

# 중식 가격
chinese = 6000

# 양식 가격
western = 8500

# 할인된 한식의 가격
discount_korean = int(korean * 0.9)

# 전체 예산을 계산하여 저장
total_price = discount_korean * 55 + chinese * 43 + western * 52

# 값을 확인
print("한식 : " + str(korean))
print("중식 : " + str(chinese))
print("양식 : " + str(western))
print("할인된 한식 : " + str(discount_korean))
print("전체 예산 : " + str(total_price))
