#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max:int = 0
        prev: int = prices[0]
        for i in prices:
            profit:int = i - prev
            if profit > 0:
                max += profit
            prev = i
        return max

# @lc code=end

