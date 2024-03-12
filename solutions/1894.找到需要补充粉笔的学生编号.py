#
# @lc app=leetcode.cn id=1894 lang=python3
#
# [1894] 找到需要补充粉笔的学生编号
#

# @lc code=start
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        full_sum = 0
        left = k
        for idx, i in enumerate(chalk):
            full_sum = full_sum + i
            left = k - full_sum
            if left < 0:
                return idx
        left = left % full_sum
        if left == 0:
            return 0
        for idx, i in enumerate(chalk):
            left = left - i
            if left < 0:
                return idx
            if left == 0:
                return idx + 1
            

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    chalk = [5,1,5]
    k = 22
    print(s.chalkReplacer(chalk, k))
    chalk = [3,4,1,2]
    k = 25
    print(s.chalkReplacer(chalk, k))

