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
        self.grid = grid
        self.max_row = len(grid) - 1
        self.max_col = len(grid[0]) - 1
        step = 0
        required_step = self.count_step([0,0], [self.max_row, self.max_col], self.grid)
        prev_required_step = required_step
        while required_step > 0:
            step += 1
            expanded = self.expand()
            prev_required_step = required_step
            required_step = self.count_step([0,0], [self.max_row, self.max_col], self.grid)
            if expanded == 0 and required_step > 0:
                return 1e9
        minutes = step- prev_required_step
        return minutes if minutes > 0 else -1
    
    def expand(self):
        edge_cells = []
        expanded = 0
        for rowIndex, row in enumerate(self.grid):
            for colIndex, cell in enumerate(row):
                if cell == 1:
                    edge_cells.extend(self.get_next_cells([rowIndex, colIndex], self.grid))
        for i in edge_cells:
            self.grid[i[0]][i[1]] = 1
            expanded += 1
        return expanded

    def count_step(self, pointA: List[int], pointB: List[int], cur_grid: List[List[int]]):
        cloned = [self.clone(i) for i  in cur_grid]
        next_cells = self.get_next_cells(pointA, cloned)
        cloned[pointA[0]][pointA[1]] = 9
        step = 1
        while len(next_cells) > 0:
            new_next = []
            for i in next_cells:
                cloned[i[0]][i[1]] = 9
                new_next.extend(self.get_next_cells(i, cloned))
            step += 1
            next_cells = new_next
            if pointB in next_cells:
                return step
        return -1

    def clone(self, l: List[any]):
        return [i for i in l]

    def get_next_cells(self, cell: List[int], grid: List[List[int]]):
        return list(
            filter(
                lambda x: x[0] >=0 and x[0] <= self.max_row and x[1] >=0 and x[1] <= self.max_col and grid[x[0]][x[1]] == 0 ,
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
    grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
    print(s.maximumMinutes(grid))

