#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 3:
            return False
        left = n
        while left > 1:
            print(left)
            remain = n % 3
            if remain != 0:
                return False
            left = left / 3
            if left == 1:
                return True
        return False
# @lc code=end

