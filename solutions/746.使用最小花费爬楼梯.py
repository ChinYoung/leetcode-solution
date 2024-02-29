#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        cost_log = [0,0,]
        for idx in range(2, len(cost)):
            cost_log.append(min(cost[idx - 1] + cost_log[idx-1], cost[idx - 2] + cost_log[idx - 2]))
        return min(cost[-1] + cost_log[-1], cost[-2] + cost_log[-2])



# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))
    print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))