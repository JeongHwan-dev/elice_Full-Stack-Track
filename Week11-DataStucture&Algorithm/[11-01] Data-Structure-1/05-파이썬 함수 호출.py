def dataCalc1(data):
    data = data + 1


def dataCalc2(data):
    data[0] = data[0] + 1


def main():
    data1 = 1
    data2 = [1]

    # Call by value
    dataCalc1(data1)
    print(f'data1: {data1}')

    # Call by reference
    dataCalc2(data2)
    print(f'data2: {data2}')


if __name__ == '__main__':
    main()