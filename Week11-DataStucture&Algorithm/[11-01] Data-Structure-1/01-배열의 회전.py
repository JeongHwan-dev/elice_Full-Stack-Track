"""
[입력]
[1, 2, 3, 4, 5, 6, 7, 8, 9], 4

[출력]
[6,7,8,9,1,2,3,4,5]
"""


def partialReverse(nums, start, end):
    for i in range(0, int((end - start)/2) + 1):
        temp = nums[start + i]
        nums[start + i] = nums[end - i]
        nums[end - i] = temp


def rotateArray(nums, k):
    return nums[-k:] + nums[:-k]


def main():
    nums = [1, 2, 3, 4, 5, 6]
    partialReverse(nums, 1, 2)

    print(nums)
    print(rotateArray([1, 2, 3, 4, 5, 6, 7, 8, 9, ], 4))


if __name__ == '__main__':
    main()
