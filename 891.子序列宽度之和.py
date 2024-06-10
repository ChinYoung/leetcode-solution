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
        mod = 1e9 + 7
        first = nums[0]
        acc_map = {}
        acc_map[first] = {}
        acc_map[first][first] = 1
        for i in nums[1:]:
            for start in list(acc_map.keys()):
                num_map = acc_map[start]
                for end in list(num_map.keys()):
                    count = num_map[end]
                    if i < start:
                        i_map = acc_map.setdefault(i, {})
                        try:
                            i_map[end] = acc_map[i][end] + count
                        except:
                            i_map[end] = i_map.setdefault(end, 0) + count
                        continue
                    if i > end:
                        i_map = acc_map.setdefault(start, {})
                        i_map[i] = i_map.setdefault(i, 0) + count
                        continue
                    acc_map[start][end] += count
            i_map = acc_map.setdefault(i, {})
            i_map[i] = i_map.setdefault(i, 0) + 1
            print(acc_map)
        res = 0
        total = 0
        for start in acc_map.keys():
            num_map = acc_map[start]
            for end in num_map.keys():
                count = num_map[end]
                total += count
                res += abs(start - end) * count
                res = res % mod
        print(total)
        return int(res)

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # nums = [2,1,3]
    # print(s.sumSubseqWidths(nums))
    # nums = [2]
    # print(s.sumSubseqWidths(nums))
    # nums = [1,3,8,5]
    # print(s.sumSubseqWidths(nums))
    # nums = [3,7,2,3]
    # print(s.sumSubseqWidths(nums))
    # nums = [7,8,8,10,4]
    # print(s.sumSubseqWidths(nums))
    nums = [7,5,8,5,7,4]
    print(s.sumSubseqWidths(nums))