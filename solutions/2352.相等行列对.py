#
# @lc app=leetcode.cn id=2352 lang=python3
#
# [2352] 相等行列对
#

# @lc code=start
from typing import Dict, List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        gridMapByRow = {}
        for row in grid:
            eleMap: Dict = gridMapByRow
            for index, i in enumerate(row):
                if index == len(row) - 1:
                    eleMap[i] = eleMap.setdefault(i, 0) + 1
                else:
                    eleMap = eleMap.setdefault(i, {})
        colIndex = 0
        maxIndex = len(grid[0]) - 1
        result = 0
        # print(gridMapByRow)
        while colIndex <= maxIndex:
            path = gridMapByRow
            rowCount = None
            for index, row in enumerate(grid):
                try:
                    ele = row[colIndex]
                    path = path[ele]
                    # print(ele)
                    if index == len(grid) - 1:
                        rowCount = path
                except KeyError:
                    rowCount = 0
                    break
            result += rowCount
            colIndex += 1
        return result


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
    print(s.equalPairs(
        [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
    print(s.equalPairs([[3, 1, 2, 2, 6], [1, 4, 4, 5, 7], [
          2, 4, 2, 2, 3], [2, 4, 2, 2, 3], [6, 4, 3, 2, 9]]))
