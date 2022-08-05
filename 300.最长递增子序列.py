#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        recorder = [1] * len(nums)
        for i_index, i in enumerate(nums):
            for j_index, j in enumerate(nums[:i_index]):
                if j < i:
                    recorder[i_index] = max(recorder[j_index] + 1, recorder[i_index])
        return (max(recorder))
# @lc code=end

