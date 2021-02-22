"""
[지시사항]
1. find_seven 함수의 매개변수로 리스트 하나만 입력받도록 수정하고 해당 리스트에서 7의 개수를 찾아 반환하세요.
    - 매개변수 입력 예시
        [7, 4, 7]
    - 함수 변환 예시
        2
"""


def find_seven(sample_list):
    count_seven = 0

    for i in range(len(sample_list)):
        if sample_list[i] == 7:
            count_seven += 1

    return count_seven


list1 = [7, 4, 7, 7, 7, 5]
print(find_seven(list1))
