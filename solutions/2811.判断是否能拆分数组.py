#
# @lc app=leetcode.cn id=2811 lang=python3
#
# [2811] 判断是否能拆分数组
#

# @lc code=start


from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) < 3:
            return True
        prev = nums[0]
        for i in nums[1:]:
            if prev+i >=m:
                return True
            prev = i
        return False
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    nums = [2, 1, 3]
    m = 5
    print(s.canSplitArray(nums, m))
    nums = [2, 2, 1]
    m = 4
    print(s.canSplitArray(nums, m))
    nums = [2, 3, 3, 2, 3]
    m = 6
    print(s.canSplitArray(nums, m))