#
# @lc app=leetcode.cn id=2348 lang=python3
#
# [2348] 全 0 子数组的数目
#

# @lc code=start
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        logList = []
        count = 0
        for i in nums:
            if i == 0:
                count += 1
            elif count > 0:
                logList.append(count)
                count = 0
        if count > 0:
            logList.append(count)
        res = 0
        for i in logList:
            res += self.getTotalCount(i)
        return res

    def getTotalCount(self, length):
        return sum(range(1, length+1))
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]))
    print(s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))
    print(s.zeroFilledSubarray([2, 10, 2019]))
