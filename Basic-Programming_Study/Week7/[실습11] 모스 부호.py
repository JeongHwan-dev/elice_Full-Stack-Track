"""
[지시사항]
1. 알파벳 26자에 대응되는 Morse Code가 주어진다.
2. Morse Code에는 각 알파벳에 대응되는 Morse Code가 중복되기도 한다.
3. 중복된 모스부호는 하나만 출력하기로 한다.
4. 알파벳 리스트인 word를 모스부호로 출력해보도록 해요.
5. 출력 값은 changed_words의 갯수를 반환한다.
"""


def uniqueMorseRepresentation(words):
    # 알파벳을 키로 가지고 모스 부호를 value 로 가지는 딕셔너리를 생성하세요.
    morse_code = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
                  'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.",
                  'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
                  'y': "-.--", 'z': "--.."}

    changed_words = []

    for i in range(len(words)):
        piece = []
        for j in range(len(words[i])):
            piece.append(morse_code[words[i][j]])
        word = ''.join(piece)
        changed_words.append(word)
    # 중복을 제거하기 위해 set 을 이용합니다.
    changed_words_set = set(changed_words)

    # 알파벳을 모스부호로 변환한 후 set 의 길이를 반환해줍니다.
    return len(changed_words_set)


# 아래의 변수 및 코드는 수정하지 마시오.
words = ["gin", "zen", "gin", "msg"]
print(uniqueMorseRepresentation(words))
