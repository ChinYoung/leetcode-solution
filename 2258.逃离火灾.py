#
# @lc app=leetcode.cn id=2258 lang=python3
#
# [2258] 逃离火灾
#

# solution
# 火先扩散, 每次扩散时, 给人一个“步”, 检查以当前“步”数能否一次性走到安全屋,如果可以则是安全的
# 下一步火扩散至不能走到安全屋时, 即为最后的机会, 当前走到安全屋花费的掉必要步数后剩下的就是最大可等待的时间

# @lc code=start
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        MAX = int(1e9)
        self.safe_row = len(grid)-1
        self.safe_col = len(grid[0])-1
        grid[self.safe_row][self.safe_col] == -1
        self.fire_map = self.generate_fire_map(grid)
        step = 1
        options = [[[row, col], self.clone(grid), MAX if self.fire_map[row][col] == 0 else self.fire_map[row][col] - 1 - step] for [row, col] in self.get_next_cells([0,0], grid)]
        res = []
        path_gap_log = {}
        while len(options) > 0:
            step += 1
            new_next = []
            new_next_map = {}
            for [cell, moved_grid, gap] in options:
                if gap < 0:
                    continue
                next_cells = self.get_next_cells(cell, moved_grid)
                for [row, col] in next_cells:
                    id = str(row) + ',' + str(col)
                    if new_next_map.setdefault(id, None) != None:
                        pass
                    new_grid = self.clone(moved_grid)
                    new_grid[row][col] = 5
                    allowed_gap = MAX if gap == MAX and self.fire_map[row][col] ==0 else min(gap, self.fire_map[row][col]-1-step)
                    if row == self.safe_row and col == self.safe_col:
                        allowed_gap = MAX if gap == MAX else min(gap, self.fire_map[row][col]-step)
                        res.append(allowed_gap)
                        continue
                    new_next_map[id] = True
                    new_next.append([[row,col], new_grid, allowed_gap])
            options = new_next
        if len(res) == 0:
            return -1
        return max(res) if max(res) >=0 else -1

    def clone(self, grid:List[List[int]]):
        return [[j for j in i] for i in grid]
    
    def generate_fire_map(self, grid: List[List[int]]):
        fire_map = self.clone(grid)
        cloned_grid = self.clone(grid)
        expanded = self.expand(cloned_grid)
        step = 1
        for [row, col] in expanded:
            fire_map[row][col] = step
        while len(expanded) > 0:
            expanded = self.expand(cloned_grid)
            step += 1
            for [row, col] in expanded:
                fire_map[row][col] = step
        return fire_map
    
    def expand(self, grid: List[List[int]]):
        edge_cells = []
        for rowIndex, row in enumerate(grid):
            for colIndex, cell in enumerate(row):
                if cell == 1:
                    edge_cells.extend(self.get_next_cells([rowIndex, colIndex], grid))
        for [row,col] in edge_cells:
            grid[row][col] = 1
        return edge_cells

    def get_next_cells(self, cell: List[int], grid: List[List[int]]):
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        return list(
            filter(
                lambda x: x[0] >=0 and x[0] <= max_row and x[1] >=0 and x[1] <= max_col and grid[x[0]][x[1]] == 0 ,
                [
                    [cell[0]+1, cell[1]],
                    [cell[0]-1, cell[1]],
                    [cell[0], cell[1]+1],
                    [cell[0], cell[1]-1],
                ]
            )
        )


# @lc code=end
if __name__ =="__main__":
    s = Solution()
    # grid = [[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]]
    # print(s.maximumMinutes(grid))
    # grid = [[0,1],[0,2],[0,0],[2,0]]
    # print(s.maximumMinutes(grid))
    grid = [[0,2,0,0,0,0,0,0,0,2,0,2,0,2,2,0,2,0,0,0,0,0],[0,0,0,2,2,2,0,2,0,0,0,0,0,0,0,0,0,0,2,2,2,2],[0,2,2,2,2,2,2,2,2,0,2,2,2,0,2,2,2,0,0,2,0,2],[0,0,2,0,0,0,2,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0],[2,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,2,0],[0,0,2,0,2,0,2,2,0,0,0,2,2,2,2,0,2,2,0,0,2,0],[2,2,2,0,2,2,2,2,2,2,0,0,0,0,2,0,0,2,2,0,2,0],[0,0,0,0,0,0,0,0,0,2,0,2,0,2,2,2,2,2,2,0,2,0],[2,0,2,0,2,0,2,0,2,2,0,2,0,0,0,0,2,0,2,0,2,2],[0,0,2,0,2,0,2,0,2,2,0,2,2,0,2,0,0,0,2,2,2,2],[0,2,2,0,2,0,2,0,2,1,0,0,2,2,2,0,2,0,0,2,0,0],[0,2,2,0,2,2,2,0,2,2,2,0,0,0,2,0,2,2,0,0,0,2],[0,2,2,0,2,0,0,0,0,0,2,2,0,2,2,2,1,2,2,0,2,1],[0,2,2,0,2,2,2,0,2,0,2,2,0,0,0,0,2,2,0,0,0,2],[0,2,0,0,2,0,0,0,2,0,2,0,0,2,0,2,2,0,0,2,0,0],[2,2,2,0,2,2,0,2,2,0,2,2,0,2,2,2,2,2,0,2,2,0],[0,0,0,0,2,2,0,2,0,0,2,2,0,0,0,0,0,2,0,2,0,0]]
    print(s.maximumMinutes(grid))

