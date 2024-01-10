#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # k为1, 不需要拆分
        if k == 1:
            return True
        sum_value = sum(nums)
        # 无法均分, 直接返回False
        if sum_value % k != 0:
            return False
        sorted_list = sorted(nums, reverse=True)
        # 均值, 即各子集的目标值
        average = sum_value / k
        all_grp = self.findAllList(sorted_list, average)
        # 没有有效的子集, 返回False
        if len(all_grp) == 0:
            return False
        for grp in all_grp:
            # 递归检查 (差集, k-1) 是否满足要求
            remain_res =  self.canPartitionKSubsets(self.getDifference(nums, grp), k - 1)
            if remain_res:
                return True
        return False

    # 获取差集
    def getDifference(self, origin:List[int], part:List[int]):
        copy_list = origin.copy()
        for i in part:
            copy_list.remove(i)
        return copy_list

    # 获取所有和为target的子集
    def findAllList(self, nums: List[int], target):
        res = []
        handled_list = []
        for index, i in enumerate(nums):
            # 去重
            if i in handled_list:
                continue
            handled_list.append(i)
            # 大于目标值, 跳过
            if i > target:
                continue
            # 等于目标值, 直接返回list
            if i == target:
                res.append([i])
                continue
            # 从剩余index + 1开始的子集中查找和为target - i的子集
            other = nums.copy()[index+1:]
            matched_list = self.findAllList(other, target - i)
            if len(matched_list) == 0:
                continue
            for grp in matched_list:
                res.append([i] + grp)
        return res

# @lc code=end

