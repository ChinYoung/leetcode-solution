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
        prev_acc = 0
        acc_map = {}
        acc_map[first] = {}
        acc_map[first][first] = 1
        for i in nums[1:]:
            new_map = {}
            delta = 0
            for start in acc_map.keys():
                num_map = acc_map[start]
                for end in num_map.keys():
                    count = num_map[end]
                    gap = end - start
                    new_map[start] = new_map.setdefault(start, {})
                    new_map[start][end] = new_map[start].setdefault(end, count)
                    if i < start:
                        delta += (end - i) * count
                        i_map = new_map.setdefault(i, {})
                        try:
                            i_map[end] = acc_map[i][end] + count
                        except:
                            i_map[end] = i_map.setdefault(end, 0) + count
                        continue
                    if i > end:
                        delta += (i - start) * count
                        i_map = new_map.setdefault(start, {})
                        try:
                            i_map[i] = acc_map[start][i] + count
                        except:
                            i_map[i] = i_map.setdefault(i, 0) + count
                        continue
                    new_map[start][end] += count
                    delta += gap * count
            i_map = new_map.setdefault(i, {})
            i_map[i] = i_map.setdefault(i, 0) + 1
            acc_map = new_map
            # print(acc_map)
            prev_acc = int((prev_acc + delta) % mod)
        return prev_acc


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    nums = [2,1,3]
    print(s.sumSubseqWidths(nums))
    nums = [2]
    print(s.sumSubseqWidths(nums))
    nums = [1,3,8,5]
    print(s.sumSubseqWidths(nums))
    nums = [3,7,2,3]
    print(s.sumSubseqWidths(nums))
    nums = [7,8,8,10,4]
    print(s.sumSubseqWidths(nums))