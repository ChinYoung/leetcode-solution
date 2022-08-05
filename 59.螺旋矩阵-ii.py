#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        delta = [0, 1]
        x = 0
        y = 0
        cur = 0
        layer = 0
        result = [[-1 for i in range(n)] for _ in range(n)]
        while result[x][y] == -1:
            cur = cur + 1
            result[x][y] = cur
            print(x, y)
            if y == layer and x == layer + 1:
                y = y + 1
                layer = layer + 1
                delta = [0, 1]
                continue
            if x == layer and y == layer:
                delta = [0, 1]
            if y == n - 1 - layer and x == layer:
                delta = [1, 0]
            if y == n - 1 - layer and x == n - 1 - layer:
                delta = [0, -1]
            if y == layer and x == n - 1 - layer:
                delta = [-1, 0]
            x = x + delta[0]
            y = y + delta[1]
        return result
# @lc code=end

