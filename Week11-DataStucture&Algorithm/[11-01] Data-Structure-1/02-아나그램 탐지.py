"""
[아나그램(Anagram)]
한 문자열의 문자를 재배열해서 다른 뜻을 가지는 다른 단어로 바꾸는 것을 의미한다.
"""


def isAnagram(str1, str2):
    return sorted(str1) == sorted(str2)


def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle'))
    print(isAnagram('cat', 'cap'))


if __name__ == "__main__":
    main()
