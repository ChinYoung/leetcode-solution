#
# @lc app=leetcode.cn id=2706 lang=python3
#
# [2706] 购买两块巧克力
#
from typing import List

# @lc code=start


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = prices[0]
        second = prices[1]
        for i in prices[2:]:
            if i < first:
                if second > first:
                    second = i
                else:
                    first = i
            elif i < second:
                second = i
        return money - first - second if first+second<=money else money
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.buyChoco([69,91,78,19,40,13], 94))

