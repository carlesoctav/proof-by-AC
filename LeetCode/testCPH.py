from typing import List


def maxScoreIndices(nums: List[int]) -> List[int]:
    list_of_sum = []
    num_of_1s = sum(nums)
    num_of_0s = len(nums) - num_of_1s
    list_of_sum.append(num_of_1s)

    dp_0 = [0 for i in range(len(nums))]
    dp_1 = [0 for i in range(len(nums))]

    nums_reverse = nums[::-1]
    print(f"==>> nums_reverse: {nums_reverse}")

    if nums[0] == 0:
        dp_0[1] += 1

    if nums_reverse[1] == 1:
        dp_1[1] += 1

    for i in range(1, len(nums) - 1):
        if nums[i] == 0:
            dp_0[i + 1] = dp_0[i] + 1

    for i in range(1, len(nums) - 1):
        if nums_reverse[i] == 1:
            dp_1[i + 1] = dp_1[i] + 1

    print(f"==>> dp_1: {dp_1}")
    print(f"==>> dp_0: {dp_0}")

    dp_1 = dp_1[::-1]

    for i in range(1, len(nums) - 1):
        list_of_sum.append(dp_0[i] + dp_1[i])

    list_of_sum.append(num_of_0s)

    print(list_of_sum)
    return list_of_sum


def main():
    list = [0, 0, 1, 0]
    maxScoreIndices(list)


main()
