"""
[지시사항]
1. 반복문 아래에 들여쓰기를 4칸으로 수정하세요.
2. 딕셔너리가 선언된 부분과 반복문이 사용된 부분 사이에 줄바꿈을 추가하세요.
3. a, b, i라고 정의된 이름을 의미 있는 이름으로 수정하세요.
  - 변수명 a를 original_texts 로 수정하세요.
  - 변수명 b를 minions_dictionary 로 수정하세요.
3. 4번째 줄 딕셔너리가 호출된 부분의 괄호 띄어쓰기를 올바르게 수정하세요.
"""

original_texts = ["Bello", "Bello", "Tulaliloo_ti_amo", "Tank_yu", "Poopaye", "Poopaye"]
minions_dictionary = {"Bello": "안녕", "Tulaliloo_ti_amo": "우린 너를 사랑해", "Poopaye": "잘가", "Tank_yu": "고마워"}

for text in original_texts:
    print(minions_dictionary[text])
