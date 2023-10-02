#

# @lc app=leetcode id=2155 lang=python3
#
# [2155] All Divisions With the Highest Score of a Binary Array
#


# @lc code=start
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        list_of_sum = []
        num_of_1s = sum(nums)
        num_of_0s = len(nums) - num_of_1s
        list_of_sum.append(num_of_0s)

        dp_0 = [0 for i in range(len(nums))]
        dp_1 = [0 for i in range(len(nums))]

        nums_reverse = nums.reverse()

        if nums[0] == 0:
            dp_0[0] += 1

        if nums_reverse[0] == 1:
            dp_1[0] += 1

        for i in range(len(nums)):
            if nums[i] == 0:
                dp_0[i] = dp_0[i - 1] + 1
        for i in range(len(nums)):
            if nums_reverse[i] == 1:
                dp_1[i] = dp_1[i - 1] + 1

        for i in range(len(nums)):
            list_of_sum.append(dp_0[i] + dp_1[len(nums) - i])

        return list_of_sum


# @lc code=end
