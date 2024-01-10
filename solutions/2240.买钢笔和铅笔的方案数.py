#
# @lc app=leetcode.cn id=2240 lang=python3
#
# [2240] 买钢笔和铅笔的方案数
#
import math
# @lc code=start
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        max_1 = math.floor(total/cost1)
        count = 0
        for i in range(max_1 + 1):
            left_money = total - i * cost1
            max_2 = math.floor(left_money/cost2)
            count += (max_2 + 1)
        return count
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.waysToBuyPensPencils(20, 10, 5))

