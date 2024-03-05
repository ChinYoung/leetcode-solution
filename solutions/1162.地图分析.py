#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析

# 烂橘子算法, 边缘扩张, 直至没有可以继续扩张的区块, 则可以实现最后扩张的cell为“距其最近的1的距离值最大”
#

# @lc code=start
from typing import List
import time


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.max_row = len(grid) - 1
        self.max_col = len(grid[0]) - 1
        edges = []
        res = -1
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if self.isEdge(row, col):
                    edges.append([row, col])
        while len(edges) > 0:
            res = res + 1 if res != -1 else 1
            extended_cells = []
            for [row, col] in edges:
                created_edges = self.grow(row, col)
                if len(created_edges) > 0:
                    extended_cells.extend(created_edges)
            edges = list(filter(lambda x: self.isEdge(x[0], x[1]), extended_cells))
        return res

    def isEdge(self, row: int, col):
        if self.grid[row][col] != 1:
            return False
        for [row_no, col_no] in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
            if not (row_no >=0 and col_no >= 0 and row_no <= self.max_row and col_no <= self.max_col):
                continue
            if self.grid[row_no][col_no] == 0:
                return True
        return False

    def grow(self, row: int, col: int):
        res = []
        for [row_no, col_no] in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
            if not (row_no >=0 and col_no >= 0 and row_no <= self.max_row and col_no <= self.max_col):
                continue
            if self.grid[row_no][col_no] == 0:
                self.grid[row_no][col_no] = 1
                res.append([row_no, col_no])
        return res

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    x = [[1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0],[1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1],[0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0],[0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1],[1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0],[0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0],[1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1],[0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0],[1,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0],[0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0],[0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0],[0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1],[1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1],[1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0],[1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1],[0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0]]
    print(s.maxDistance(x))
    x = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    print(s.maxDistance(x))
    x = [[1,0,0],[0,0,0],[0,0,0]]
    print(s.maxDistance(x))
    x = [[1,0,1],[0,0,0],[1,0,1]]
    print(s.maxDistance(x))



