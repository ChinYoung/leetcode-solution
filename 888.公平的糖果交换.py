#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceMap = {}
        bobMap = {}
        aliceTotal = 0
        bobTotal = 0
        for i in aliceSizes:
            aliceMap[i] = True
            aliceTotal += i
        for j in bobSizes:
            bobMap[j] = True
            bobTotal += j
        expect = int((aliceTotal+bobTotal) * 0.5 - aliceTotal)
        # print(aliceTotal, bobTotal, expect)
        for i in aliceSizes:
            if bobMap.setdefault(i+expect, False):
                    return [i, i + expect]

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.fairCandySwap([1,1], [2,2]))
    print(s.fairCandySwap([1,2,5], [2,4]))

