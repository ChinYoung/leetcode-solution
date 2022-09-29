#
# @lc app=leetcode.cn id=769 lang=python3
#
# [769] 最多能完成排序的块
#

# @lc code=start
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedList = sorted(arr)
        expecting = []
        actual = []
        res = 0
        for index, i in enumerate(arr):
            if len(expecting) == 0 and i == sortedList[index]:
                expecting = []
                actual = []
                res += 1
                continue
            expecting.append(sortedList[index])
            actual.append(i)
            # print(i, sortedList[index], expecting, actual)
            if expecting == sorted(actual):
                res += 1
                expecting = []
                actual = []
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.maxChunksToSorted([0, 4, 2, 3, 1]))
