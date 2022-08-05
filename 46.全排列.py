#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        max_len = len(nums)
        if max_len == 1:
            return [nums]
        result = []
        for index, i in enumerate(nums):
            other = nums[0 : index] + nums[index + 1:]
            for lst in self.permute(other):
                result.append([i] + lst)
        return list(tuple(result))
# @lc code=end

