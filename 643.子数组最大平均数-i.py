#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        numsLength = len(nums)
        curSum = maxSum
        for i in range(k, numsLength):
            curSum = curSum + nums[i] - nums[i - k]
            if curSum > maxSum:
                maxSum = curSum
        return maxSum / k
# @lc code=end

