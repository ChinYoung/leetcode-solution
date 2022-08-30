#
# @lc app=leetcode.cn id=1866 lang=python3
#
# [1866] 恰有 K 根木棍可以看到的排列数目
#

# @lc code=start
from typing import Dict


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        log = {}
        log[0] = {0:1, 1:0}
        for i in range(1, n+1):
            row = log.setdefault(i, {})
            prevRow:Dict[int:int] = log.setdefault(i-1, {})
            for j in range(1, k+1):
                row[j] = (prevRow.setdefault(j-1, 0) + (i-1) * prevRow.setdefault(j, 0)) % (10**9 + 7)
        return log[n][k]

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.getPossibilities(4, 2))
    print(s.rearrangeSticks(20,11))
    print(s.rearrangeSticks(105,20))
