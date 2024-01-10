#
# @lc app=leetcode.cn id=1975 lang=python3
#
# [1975] 最大方阵和
#

# @lc code=start
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negList = []
        absList = []
        total = 0
        hasZero = False
        for ls in matrix:
            for i in ls:
                absValue = abs(i)
                absList.append(absValue)
                total += absValue
                hasZero = hasZero or i == 0
                if i < 0:
                    negList.append(i)
        if hasZero:
            return total
        if len(negList) % 2 == 0:
            return total
        return total + 2 * sorted(absList)[0] * -1
# @lc code=end

