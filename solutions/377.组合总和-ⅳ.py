#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        num_map = {}
        num_map[0] = 1
        for i in range(1, target+1):
            for j in nums:
                num_map[i] = num_map.setdefault(i, 0) + num_map.setdefault(i-j, 0)
        return num_map[target]

            

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    target = 4
    print(s.combinationSum4(nums, target))
    nums = [9]
    target = 3
    print(s.combinationSum4(nums, target))


