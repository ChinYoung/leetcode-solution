#
# @lc app=leetcode.cn id=2178 lang=python3
#
# [2178] 拆分成最多数目的正偶数之和
#

# @lc code=start
from math import floor
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        half = finalSum / 2
        max = 0
        sum = 0
        while sum < half:
            max += 1
            sum = self.getSum(max)
        if sum == half:
            return [2*(i + 1) for i in range(max)]
        gap = half - self.getSum(max - 1)
        result = []
        for i in reversed(range(max-1)):
            result.append(2 * (i + 1 + (1 if gap > 0 else 0)))
            gap -= 1
        return result

    def getSum(self, max):
        if max % 2 == 0:
            return (1+max) * max / 2
        return (1+max) * floor(max / 2) + (1+max) * 0.5
# @lc code=end
if __name__ =="__main__":
    s = Solution()
    print(s.maximumEvenSplit(12))
    print(s.maximumEvenSplit(28))
    print(s.maximumEvenSplit(30))
