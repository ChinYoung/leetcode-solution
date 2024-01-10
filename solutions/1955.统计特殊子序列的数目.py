#
# @lc app=leetcode.cn id=1955 lang=python3
#
# [1955] 统计特殊子序列的数目
#

# @lc code=start
from typing import List


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        f0 = f1 = f2 = 0
        mod = pow(10, 9) + 7
        for i in nums:
            if i == 0:
                f0 = (2 * f0 + 1) % mod
            if i == 1:
                f1 = (2 * f1 + f0) % mod
            if i == 2:
                f2 = (2 * f2 + f1) % mod
        return f2
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.countSpecialSubsequences([0,1,2,2]))
    print(s.countSpecialSubsequences([0,1,2,0,1,2]))

