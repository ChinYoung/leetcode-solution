#
# @lc app=leetcode.cn id=1701 lang=python3
#
# [1701] 平均等待时间
#

# @lc code=start
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        passedTime = -1
        total = 0
        for grp in customers:
            arriveTime = grp[0]
            costTime = grp[1]
            if passedTime == -1 or arriveTime > passedTime:
                passedTime = arriveTime
            total += (costTime + passedTime - arriveTime)
            passedTime += costTime
        return total / len(customers)
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
    print(s.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))
