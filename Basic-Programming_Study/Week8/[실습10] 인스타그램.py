"""
[지시사항]
1. Article 클래스의 필드 좋아요 수, 내용, 해시태그를 추가해 보세요.
2. Article 클래스에서 값을 초기화하는 메서드와 좋아요 수를 증가시키는 메서드를 추가해 보세요
"""


class Article():
    likes = int(0)
    content = ''
    hashtag = []

    def like_article(self):
        self.likes += 1

    def remove(self):
        self.likes = 0
        self.content = ''
        self.hashtag = []


insta = Article()
insta.content = "열심히 코딩 공부 하는 중"
insta.hashtag = ['엘리스', '체셔']
insta.like_article()
insta.like_article()
insta.like_article()

print(insta.content)
print(insta.hashtag)
print(insta.likes)

insta.remove()

print(insta.content)
print(insta.hashtag)
print(insta.likes)
