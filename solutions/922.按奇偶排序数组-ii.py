#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenPoint = 0
        oddPoint = 1
        new_list = [n for n in nums]
        for i in nums:
            if i % 2 == 0:
                new_list[evenPoint] = i
                evenPoint = evenPoint + 2
            else:
                new_list[oddPoint] = i
                oddPoint = oddPoint + 2
            print
        return new_list
# @lc code=end

