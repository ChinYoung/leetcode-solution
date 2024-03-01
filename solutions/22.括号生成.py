#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [['(', 1, n-1, n]]
        for i in range(2, 2 * n + 1):
            new_res = []
            for [s, open_num, l_num, r_num] in res:
                if l_num > 0:
                    new_res.append([s + '(', open_num+1, l_num - 1, r_num])
                if open_num > 0:
                    new_res.append([s + ')', open_num - 1, l_num, r_num - 1])
            res = new_res
        return [i[0] for i in res]

# @lc code=end

if __name__ =="__main__":
    s = Solution()
    print(s.generateParenthesis(5))
