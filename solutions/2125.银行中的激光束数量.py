#
# @lc app=leetcode.cn id=2125 lang=python3
#
# [2125] 银行中的激光束数量
#

# @lc code=start
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        validRows = list(filter(lambda i:i>0, [self.sum(s) for s in bank]))
        rowCount = len(validRows)
        if rowCount < 2:
            return 0
        return sum([validRows[i] * validRows[i+1] for i in range(rowCount - 1)])

    def sum(self, s:str):
        return sum(int(i) for i in s)
# @lc code=end

if __name__ =="__main__":
    s = Solution()
    print(s.numberOfBeams(["011001","000000","010100","001000"]))

