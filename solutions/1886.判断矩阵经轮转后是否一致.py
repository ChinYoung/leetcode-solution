#
# @lc app=leetcode.cn id=1886 lang=python3
#
# [1886] 判断矩阵经轮转后是否一致
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.x_max = 0
        self.y_max = 0

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        self.mat = mat
        self.x_max = len(mat[0]) - 1
        self.y_max = len(mat) - 1
        self.first_0 = [0, 0]
        self.first_90 = [0, self.y_max]
        self.first_180 = [self.x_max, self.y_max]
        self.first_270 = [self.x_max, 0]
        return self.compare([0,0],self.first_0, target, self.get_next_0) \
            or self.compare([0,0],self.first_90, target, self.get_next_90) \
            or self.compare([0,0],self.first_180, target, self.get_next_180) \
            or self.compare([0,0],self.first_270, target, self.get_next_270)

    def compare(self,mat_pos,target_pos, target, fn_target_next):
        if  self.mat[mat_pos[0]][mat_pos[1]] != target[target_pos[0]][target_pos[1]]:
            return False
        mat_next = self.get_next_0(mat_pos)
        rotate_next = fn_target_next(target_pos)
        if mat_next == None and rotate_next == None:
            return True
        return self.compare(mat_next, rotate_next,target, fn_target_next)

    # 获取旋转0度后相应的下一个坐标
    def get_next_0(self,cur):
        x = cur[0]
        y = cur[1]
        if x >= self.x_max and y >= self.y_max:
            return None
        if x >= self.x_max:
            return [0, y + 1]
        return [x + 1, y]

    # 获取旋转90度时下一个坐标
    def get_next_90(self,cur):
        x = cur[0]
        y = cur[1]
        if x >= self.x_max and y == 0:
            return None
        if y == 0:
            return [x + 1, self.y_max]
        return [x, y - 1]

    # 获取旋转180度时下一个坐标
    def get_next_180(self,cur):
        x = cur[0]
        y = cur[1]
        if x == 0 and y == 0:
            return None
        if x == 0:
            return [self.x_max, y - 1]
        return [x - 1, y]

    # 获取旋转270度时下一个坐标
    def get_next_270(self,cur):
        x = cur[0]
        y = cur[1]
        if x == 0 and y == self.y_max:
            return None
        if y == self.y_max:
            return [x - 1, 0]
        return [x, y + 1]


# @lc code=end

