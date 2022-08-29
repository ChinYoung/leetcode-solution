#
# @lc app=leetcode.cn id=1866 lang=python3
#
# [1866] 恰有 K 根木棍可以看到的排列数目
#

# @lc code=start
from typing import Dict


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        pass

    def getValidCombinations(self, exclude: Dict[int, bool], k: int, minimum: int):
        pass

    def getPossibilities(self, max:int):
        if max == 1:
            return 1
        next = self.getPossibilities(max- 1)
        return max + (max-1)*(next -1)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.getPossibilities(2))
