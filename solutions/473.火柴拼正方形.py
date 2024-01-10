#
# @lc app=leetcode.cn id=473 lang=python3
#
# [473] 火柴拼正方形
#

# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        res = self.canPartitionKSubsets(matchsticks, 4)
        return res

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        sorted_list = sorted(nums, reverse=True)
        sum_value = sum(nums)
        if sum_value % k != 0:
            return False
        average = sum_value / k
        all_grp = self.findAllList(sorted_list, average)
        if len(all_grp) == 0:
            return False
        for grp in all_grp:
            remain_res =  self.canPartitionKSubsets(self.getDifference(nums, grp), k - 1)
            if remain_res:
                return True
        return False

    def getDifference(self, origin:List[int], part:List[int]):
        copy_list = origin.copy()
        for i in part:
            copy_list.remove(i)
        return copy_list

    def findAllList(self, nums: List[int], target):
        res = []
        handled_list = []
        for index, i in enumerate(nums):
            if i in handled_list:
                continue
            handled_list.append(i)
            if i > target:
                continue
            if i == target:
                res.append([i])
                continue
            other = nums.copy()[index+1:]
            matched_list = self.findAllList(other, target - i)
            if len(matched_list) == 0:
                continue
            for grp in matched_list:
                res.append([i] + grp)
        return res
# @lc code=end

