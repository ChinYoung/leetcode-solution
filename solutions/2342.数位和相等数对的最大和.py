#
# @lc app=leetcode.cn id=2342 lang=python3
#
# [2342] 数位和相等数对的最大和
#

# @lc code=start
from typing import List
import math


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        self.numMap = {}
        maxSum = -1
        for i in nums:
            digitalSum = self.getDigitalSum(i)
            num1, num2 = self.numMap.setdefault(digitalSum, [-1, -1])
            self.numMap[digitalSum] = sorted([num1, num2, i])[1:]
            curSum = sum(self.numMap[digitalSum])
            if not -1 in self.numMap[digitalSum] and curSum > maxSum:
                maxSum = curSum
        return maxSum

    def getDigitalSum(self, num: int):
        left = num
        res = 0
        while left != 0:
            res += (left % 10)
            left = math.floor(left / 10)
        return res
# @lc code=end

if __name__ =="__main__":
    s = Solution()
    # print(s.getDigitalSum(101129))
    print(s.maximumSum([18,43,36,13,7]))
    print(s.maximumSum([10,12,19,14]))

