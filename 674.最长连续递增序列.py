#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        temp = []
        prev = -1
        this = -1
        max = 0
        for i in nums:
            this = i
            if this > prev:
                temp.append(this)
                if len(temp) > max:
                    max = len(temp)
            else:
                temp = [this]
            prev = this
        return max
# @lc code=end

