#
# @lc app=leetcode.cn id=2563 lang=python3
#
# [2563] 统计公平数对的数目
#

# @lc code=start
from typing import List
import math


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        total = 0
        sortedNums = sorted(nums)
        for i in range(len(sortedNums) - 1):
            lowerIndex = self.getLowerIndex(i, sortedNums, lower)
            upperIndex = self.getUpperIndex(i, sortedNums, upper)
            if lowerIndex != -1 and upperIndex != -1 and lowerIndex <= upperIndex:
                total += (upperIndex+1) - lowerIndex
        return total

    def getLowerIndex(self, index: int, sortedNums: List[int], lower: int):
        num = sortedNums[index]
        maxIndex = len(sortedNums) - 1
        right = maxIndex
        left = min(index + 1, maxIndex)
        if sortedNums[maxIndex] + num < lower:
            return -1
        if sortedNums[left] + num >= lower:
            return left
        while right <= maxIndex:
            if right - 1 == left and sortedNums[left] + num < lower and sortedNums[right] + num >=lower:
                return right
            if num + sortedNums[right] >= lower:
                right = left + max(int((right - left)/2), 1)
                continue
            if num + sortedNums[right] <= lower:
                left = right
                right = left + max(int((maxIndex - left) / 2), 1)
                continue
        return -1

    def getUpperIndex(self, index:int, sortedNums: List[int], upper: int):
            maxIndex = len(sortedNums) - 1
            num = sortedNums[index]
            right = maxIndex
            left = min(maxIndex, index + 1)
            if sortedNums[left] + num> upper:
                return -1
            if sortedNums[maxIndex] + num <=upper:
                return maxIndex
            while right <= maxIndex:
                if right - 1 == left and sortedNums[left] + num <= upper and sortedNums[right] + num > upper:
                    return left
                if num + sortedNums[right] <= upper:
                    left = right
                    right = left + max(int((maxIndex - left) / 2), 1)
                    continue
                if num + sortedNums[right] > upper:
                    right = left + max(int((right - left)/2), 1)
                    continue
            return -1






# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.countFairPairs([1,7,9,2,5], 0, 100))
    print(s.countFairPairs([0,1,4,4,5,7], 3, 6))
    print(s.countFairPairs([0,1,4,4,5,7], 0, 100))
    print(s.countFairPairs([1,7,9,2,5], 11, 11))
    print(s.countFairPairs([-5,-7,-5,-7,-5], -12, -12))

    # print(s.getLowerIndex(2, [0,1,3,4,5,6,7], 9))
    # print(s.getUpperIndex(2, [0,1,3,4,5,5,5,5,5,5,7], 9))
