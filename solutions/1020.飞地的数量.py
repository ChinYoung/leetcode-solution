#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.row_len = len(grid)
        self.col_len = len(grid[0])
        res = 0
        for row in range(self.row_len):
            for col in range(self.col_len):
                cell = grid[row][col]
                if cell == 0:
                    continue
                # print(x, y)
                num_1 = 1
                grid[row][col] = 0
                is_at_edge = self.is_edge_cell(row,col)
                next_cells = self.get_neighbours(row,col)
                while True:
                    if len(next_cells) == 0:
                        break
                    new_next = []
                    for [i, j] in next_cells:
                        num_1 += 1
                        is_at_edge = is_at_edge or self.is_edge_cell(i, j)
                        neighbours = self.get_neighbours(i,j)
                        new_next.extend(neighbours)
                    next_cells = new_next
                if not is_at_edge:
                    res += num_1
        return res

    def get_neighbours(self, row, col):
        neighbours = [[row, col+1], [row,col-1], [row+1,col], [row-1,col]]
        neighbour_cells = []
        for [i,j] in neighbours:
            if i>=0 and j>=0 and i < self.row_len and j < self.col_len and self.grid[i][j] == 1:
                neighbour_cells.append([i,j])
                self.grid[i][j] = 0
        return neighbour_cells

    def is_edge_cell(self, row, col):
        return row == 0 or row == self.row_len-1 or col == 0 or col == self.col_len-1

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,1]]))
    print(s.numEnclaves([[0],[1],[1],[0],[0]]))

