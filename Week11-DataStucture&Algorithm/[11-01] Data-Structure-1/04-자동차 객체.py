class Car:
    def __init__(self):
        self.speed = 0
        self.year = 2017
        self.wheel = Wheel("aluminum")
        self.color = "white"

    def speedUp(self, addSpeed):
        self.speed += addSpeed

    def speedDown(self, subSpeed):
        self.speed -= subSpeed

    def changeColor(self, newColor):
        self.color = newColor

    def wheelChange(self, newWheelType):
        self.wheel.wheelType = newWheelType


class Wheel:
    def __init__(self, newWheelType):
        self.wheelType = newWheelType


def main():
    audi = Car()

    print("고객님의 차량은 {}년에 출고되었습니다.".format(audi.year))
    print("현재 속도는 {}km/h 입니다.".format(audi.speed))

    audi.speedUp(200)
    print("변경된 속도는 {} km/h 입니다.".format(audi.speed))

    audi.speedDown(50)
    print("변경된 속도는 {} km/h 입니다.".format(audi.speed))

    print("현재 색상은 {} 입니다.".format(audi.color))

    audi.changeColor("blue")
    print("변경된 색상은 {} 입니다.".format(audi.color))

    randomWheel = Wheel("aluminum")
    print("바닥에 {} 재질의 바퀴가 떨어져 있습니다.".format(randomWheel.wheelType))

    print("현재 차량의 wheelType은 {} 입니다.".format(audi.wheel.wheelType))

    audi.wheelChange('iron')
    print("변경된 차량의 wheelType은 {} 입니다.".format(audi.wheel.wheelType))


if __name__ == "__main__":
    main()
