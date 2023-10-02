#
# @lc app=leetcode id=1986 lang=python3
#
# [1986] Minimum Number of Work Sessions to Finish the Tasks
#


# @lc code=start
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        best = [[0, 0] for i in range(2**n)]
        best[0] = [1, 0]

        for i in range(1, 1 << n):
            best[i] = [n + 1, 0]
            for j in range(n):
                if i & (1 << j):
                    option = best[i ^ (1 << j)]
                    if option[1] + tasks[j] <= sessionTime:
                        option[1] += tasks[j]
                    else:
                        option[0] += 1
                        option[1] = tasks[j]
                    best[i] = min(best[i], option, key=lambda x: x[0])

        return best[(1 << n) - 1][0]


# @lc code=end
