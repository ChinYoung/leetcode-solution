#
# @lc app=leetcode.cn id=1862 lang=python3
#
# [1862] 向下取整数对和
#

# @lc code=start
from typing import List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        maxNum = max(nums)
        counter = [0] * (maxNum + 1)
        numSet = set()
        for i in nums:
            counter[i] += 1
            numSet.add(i)
        result = 0
        for num in numSet:
            maxFloor = int(maxNum/num)
            currentResult = 0
            possibleValue = 1
            # print(num)
            while possibleValue <= maxFloor:
                start = num * possibleValue
                end = num * (possibleValue + 1)
                # print(' ', start, end)
                for j in range(start, min([end, maxNum + 1])):
                    currentResult += (possibleValue * counter[j])
                possibleValue += 1
            currentResult = (currentResult * counter[num]) % 1000000007
            result = result + currentResult
            result = result % 1000000007
        return result
# @lc code=end

if __name__ =="__main__":
    s = Solution()
    print(s.sumOfFlooredPairs([2,5,9]))
    print(s.sumOfFlooredPairs([7,7,7,7,7,7,7]))

