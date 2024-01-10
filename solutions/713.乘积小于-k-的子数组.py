#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        total = 0
        start = 0
        end = 0
        product = nums[0]
        if product < k:
            total += (end - start + 1)
        max = len(nums) - 1
        while start <= max:
            # 检查当前子数组积是否小于 k
            if product < k:
                # print(product, start, end)
                # 未抵达队列尾, 扩张
                if end < max:
                    end += 1
                    product *= nums[end]
                    if product < k:
                        total += (end - start + 1)
                    continue
                # 抵达队列尾部, 结束
                else:
                    break
            else:
                # 起点与终点不重合,移动起点进行收缩并检查
                if start < end:
                    product = product / nums[start]
                    start += 1
                    if product < k:
                        total += (end - start + 1)
                    continue
                # 起点与终点重合, 一起后移并检查
                else:
                    start += 1
                    if start <= max:
                        end = start
                        product = nums[start]
                        if product < k:
                            total += 1
                    else:
                        break
        return total


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
    print(s.numSubarrayProductLessThanK([1,2,3], 0))
    print(s.numSubarrayProductLessThanK([1,1,1], 2))
