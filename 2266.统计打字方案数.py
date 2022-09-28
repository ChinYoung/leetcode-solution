#
# @lc app=leetcode.cn id=2266 lang=python3
#
# [2266] 统计打字方案数
#

# @lc code=start
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        p1 = 1
        p2 = 2
        p3 = 4
        p4 = 7
        pass

    def getPossibility(self, length, max):
        if length == 1 or max == 1:
            return 1


1, 1         1    2
11          1    2

###
1, 1, 1     1    2
1, 11,     1    2
11, 1      1    2
111       1    1

1, 1, 1, 1     1    2
1, 1, 11      1    2
1, 11, 1      1    2
1, 111       1    1
11, 1, 1      1    2
11, 11       1    2
111, 1       1    2

###

1: [1, 0, 0]  1
2: [1, 1, 0]  2
3: [2, 1, 1]  4
4: [4, 2, 1]  7
5: [7, 4, 2]  13
# @lc code=end
