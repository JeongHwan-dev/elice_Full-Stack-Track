"""
[지시사항]
1. 인자로는 두명이 낸 숫자들이 저장된 리스트가 들어옵니다.
2. player1이 이겼을 경우, player1 승리!를 반환합니다.
3. player2이 이겼을 경우, player2 승리!를 반환합니다.
4. 서로 비겼을 경우, 서로 비겼습니다.를 반환합니다.
5. 둘중 하나가 낸 숫자에서 중복된 것이 있거나 1~6이 아닌수가 있을경우, 동작그만 밑장빼기냐?를 반환합니다.
"""


def num_fight(player1, player2):
    score1 = 0
    score2 = 0

    if ran_check(player1) and ran_check(player2):
        for i in range(6):
            if dup_check(player1, i) and dup_check(player2, i):
                if player1[i] > player2[i]:
                    score1 += 1
                elif player1[i] < player2[i]:
                    score2 += 1
                else:
                    pass
            else:
                return "동작그만 밑장빼기냐?"
    else:
        return "동작그만 밑장빼기냐?"

    return judge(score1, score2)


def ran_check(player):
    for n in player:
        if n not in [1, 2, 3, 4, 5, 6]:
            return False
    return True


def dup_check(player, i):
    for n in range(0, i):
        if player[i] == player[n]:
            return False
    return True


def judge(point1, point2):
    if point1 > point2:
        return "player1 승리!"
    elif point1 < point2:
        return "player2 승리!"
    else:
        return "서로 비겼습니다."


print(num_fight([1, 3, 2, 4, 5, 6], [2, 3, 1, 4, 6, 5]))
