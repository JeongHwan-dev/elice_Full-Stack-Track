'''
[지시 사항]
1. Animal 클래스를 만들고 아래 코드를 클래스 내에 추가하세요.
    멤버 변수
    species = "모르는 동물"

    멤버 함수
    def say(self):
    print(self.species + "입니다.")

2. Animal 클래스를 상속받은 Dog 클래스를 만들고 species의 값을 강아지로 설정하세요.

3. Animal 클래스를 상속받은 Cat 클래스를 만들고 species의 값을 고양이로 설정하세요.

4. Dog 클래스와 Cat 클래스의 인스턴스를 만들고 각각 say() 함수를 호출하세요.

[출력 예시]
    강아지입니다.
    고양이입니다.
'''


class Animal():
    species = "모르는 동물"

    def say(self):
        print(self.species + "입니다.")


class Dog(Animal):
    species = '강아지'


class Cat(Animal):
    species = '고양이'


dog = Dog()
dog.say()

cat = Cat()
cat.say()