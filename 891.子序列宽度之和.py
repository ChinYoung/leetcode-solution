#
# @lc app=leetcode.cn id=891 lang=python3
#
# [891] 子序列宽度之和
#

from typing import List
# @lc code=start


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        # [sum, num, count]
        prev = [0, nums[0], 1]
        acc_list = [prev]
        for idx, i in enumerate(nums):
            if idx == 0:
                continue
            s = prev[0]
            for [_s, j, c] in acc_list:
                if i > j:
                    s += c * abs(i-j)
                else:
                    s += abs(i-j)
            cur = [s, i, pow(2, idx)]
            acc_list.append(cur)
            prev = cur
        print(acc_list)
        return prev[0]

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    nums = [2,1,3]
    print(s.sumSubseqWidths(nums))
    nums = [2]
    print(s.sumSubseqWidths(nums))