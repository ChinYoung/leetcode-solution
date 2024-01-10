#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的 N 个不同整数
#

# @lc code=start
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(1, int(n/2)+1):
            result.append(i)
            result.append(-1 * i)
        if n % 2 != 0:
            result.append(0)
        return result

# @lc code=end
