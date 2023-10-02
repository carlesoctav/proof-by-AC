#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return 0
        n_bin = bin(n)[2:]
        if n_bin.count("1") == 1:
            return 1
        else:
            return 0


# binary exploit
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         return n and not (n & n - 1)

# @lc code=end
