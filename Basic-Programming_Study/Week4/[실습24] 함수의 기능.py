"""
[지시사항]
1. car_set() 함수에서 speed를 10올리고 반환하는 기능을 대신하는 함수 speed_up()을 정의하세요.
2. car_set() 함수에서 speed 출력 기능을 대신하는 함수 print_speed()를 정의하세요.
3. 주석된 코드가 정상적으로 실행되어 아래와 같은 결과가 출력되도록 하세요.
    - 차의 속도는 10 입니다.
"""


def speed_up(my_speed2):
    my_speed2 += 10
    return my_speed2


def print_speed(my_speed2):
    print("차의 속도는 " + str(my_speed2) + " 입니다.")


my_speed2 = 0
my_speed2 = speed_up(my_speed2)
print_speed(my_speed2)
