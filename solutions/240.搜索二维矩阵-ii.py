#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

from typing import List
# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_len = len(matrix)
        row_index = 0
        to_searech = []
        while row_index < matrix_len:
            row_min, row_max = matrix[row_index][0], matrix[row_index][-1]
            if row_min == target or row_max == target:
                return True
            if target > row_min and target < row_max:
                to_searech.append(matrix[row_index])
            row_index += 1
        for row in to_searech:
            if self.search_row(target, row):
                return True
        return False

    def search_row(self, target:int, row: List[int]):
        row_len = len(row)
        i, h, e = int(row_len * 0.5-0.5), 0, row_len-1
        while True:
            if e-h == 1:
                if row[e] == target:
                    return True
                if row[h] == target:
                    return True
                return False
            val = row[i]
            if val == target:
                return True
            if target > val:
                h = i
                i = h + int(0.5*(e-h))
            else:
                e = i
                i = int(0.5*(e-h))

        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(s.searchMatrix(matrix, target))
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    print(s.searchMatrix(matrix, target))

