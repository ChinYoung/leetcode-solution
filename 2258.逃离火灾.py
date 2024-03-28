#
# @lc app=leetcode.cn id=2258 lang=python3
#
# [2258] 逃离火灾
#

# solution
# 火先扩散, 每次扩散时, 给人一个“步”, 检查以当前“步”数能否一次性走到安全屋,如果可以则是安全的
# 下一步火扩散至不能走到安全屋时, 即为最后的机会, 当前走到安全屋花费的掉必要步数后剩下的就是最大可等待的时间

# @lc code=start
from typing import List, Dict


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        MAX = int(1e9)
        self.safe_row = len(grid)-1
        self.safe_col = len(grid[0])-1
        grid[self.safe_row][self.safe_col] == -1
        fire_map: Dict[Dict] = self.generate_fire_map(grid)
        gap_map:Dict[Dict] = {}
        gap_map[0] = {}
        gap_map[0][0] = MAX if fire_map[0][0] == 0 else fire_map[0][0]-1
        grid[0][0] = -1
        next_cells = [[0,0]]
        step = 0
        res = -1
        while len(next_cells) != 0:
            new_next = []
            step += 1
            for cur_cell in next_cells:
                [row, col] = cur_cell
                cur_gap = gap_map.setdefault(row, {}).setdefault(col, 0)
                cur_next = self.get_next_cells([row, col], grid)
                for next_cell in cur_next:
                    [new_row, new_col] = next_cell
                    new_gap = fire_map[new_row][new_col] - 1- step
                    if fire_map[new_row][new_col] == 0:
                        new_gap = cur_gap
                    if new_row == self.safe_row and new_col == self.safe_col:
                        new_gap += 1
                    new_gap = min(cur_gap, new_gap)
                    gap_map.setdefault(new_row, {})[new_col] = max(new_gap, gap_map.setdefault(new_row, {}).setdefault(new_col, 0))
                    if new_gap < 0:
                        continue
                    if [new_row, new_col] not in new_next:
                        new_next.append([new_row, new_col])
                    if new_row == self.safe_row and new_col == self.safe_col:
                        res = max(res, new_gap)
            for [row, col] in new_next:
                grid[row][col] = -1
            next_cells = new_next
        return res

    def clone(self, grid:List[List[int]]):
        return [[j for j in i] for i in grid]
    
    def generate_fire_map(self, grid: List[List[int]]):
        fire_map: Dict[Dict] ={}
        # cloned_map: Dict[Dict] ={}
        cloned_grid = self.clone(grid)
        on_fire = []
        step = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                fire_map.setdefault(row, {})[col] = grid[row][col]
                # cloned_map.setdefault(row, {})[col] = grid[row][col]
                if grid[row][col] == 1:
                    on_fire.append([row, col])
        while len(on_fire) > 0:
            new_on_fire = []
            step += 1
            for cell in on_fire:
                [row, col] = cell
                next = self.get_next_cells(cell, cloned_grid)
                for [i, j] in next:
                    cloned_grid[i][j] = 1
                    fire_map.setdefault(i, {})[j] = step
                new_on_fire.extend(next)
            on_fire = new_on_fire
        return fire_map
    
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
    grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
    print(s.maximumMinutes(grid))
    grid = [[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]]
    print(s.maximumMinutes(grid))
    grid = [[0,1],[0,2],[0,0],[2,0]]
    print(s.maximumMinutes(grid))
    grid = [[0,2,0,0,0,0,0,0,0,2,0,2,0,2,2,0,2,0,0,0,0,0],[0,0,0,2,2,2,0,2,0,0,0,0,0,0,0,0,0,0,2,2,2,2],[0,2,2,2,2,2,2,2,2,0,2,2,2,0,2,2,2,0,0,2,0,2],[0,0,2,0,0,0,2,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0],[2,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,2,0],[0,0,2,0,2,0,2,2,0,0,0,2,2,2,2,0,2,2,0,0,2,0],[2,2,2,0,2,2,2,2,2,2,0,0,0,0,2,0,0,2,2,0,2,0],[0,0,0,0,0,0,0,0,0,2,0,2,0,2,2,2,2,2,2,0,2,0],[2,0,2,0,2,0,2,0,2,2,0,2,0,0,0,0,2,0,2,0,2,2],[0,0,2,0,2,0,2,0,2,2,0,2,2,0,2,0,0,0,2,2,2,2],[0,2,2,0,2,0,2,0,2,1,0,0,2,2,2,0,2,0,0,2,0,0],[0,2,2,0,2,2,2,0,2,2,2,0,0,0,2,0,2,2,0,0,0,2],[0,2,2,0,2,0,0,0,0,0,2,2,0,2,2,2,1,2,2,0,2,1],[0,2,2,0,2,2,2,0,2,0,2,2,0,0,0,0,2,2,0,0,0,2],[0,2,0,0,2,0,0,0,2,0,2,0,0,2,0,2,2,0,0,2,0,0],[2,2,2,0,2,2,0,2,2,0,2,2,0,2,2,2,2,2,0,2,2,0],[0,0,0,0,2,2,0,2,0,0,2,2,0,0,0,0,0,2,0,2,0,0]]
    print(s.maximumMinutes(grid))
    grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
    print(s.maximumMinutes(grid))
    grid = [[0,0,0,0,0],[0,2,0,2,0],[0,2,0,2,0],[0,2,1,2,0],[0,2,2,2,0],[0,0,0,0,0]]
    print(s.maximumMinutes(grid))
    grid = [[0,0,0,0,0,0],[0,2,2,2,2,0],[0,0,0,1,2,0],[0,2,2,2,2,0],[0,0,0,0,0,0]]
    print(s.maximumMinutes(grid))
    grid = [[0,0,0],[2,2,0],[1,2,0]]
    print(s.maximumMinutes(grid))



