#
# @lc app=leetcode.cn id=2404 lang=python3
#
# [2404] 出现最频繁的偶数元素
#

# @lc code=start


from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        num_map = {}
        for i in nums:
            if i % 2 != 0:
                continue
            freq = num_map.setdefault(i, 0)
            new_freq = freq + 1
            num_map[i] = new_freq
        num = -1
        max = -1
        for k,v in num_map.items():
            if v > max:
                max = v
                num = int(k)
                continue
            if v == max and int(k) < num:
                num = int(k)
        return num


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.mostFrequentEven([0,1,2,2,4,4,1]))
    print(s.mostFrequentEven([4,4,4,9,2,4]))
    print(s.mostFrequentEven([29,47,21,41,13,37,25,7]))
