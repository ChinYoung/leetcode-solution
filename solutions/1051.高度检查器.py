#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len([i for i,j in zip(heights, sorted(heights)) if i != j])
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.heightChecker([1,1,4,2,1,3]))
    print(s.heightChecker([5,1,2,3,4]))
    print(s.heightChecker([1,2,3,4,5]))

