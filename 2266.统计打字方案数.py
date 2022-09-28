#
# @lc app=leetcode.cn id=2266 lang=python3
#
# [2266] 统计打字方案数
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.posMap = {4: {}, 3: {}}

    def countTexts(self, pressedKeys: str) -> int:
        pass

    def getPossibility(self, length, max):
        try:
            return self.posMap[max][length]
        except:
            log = [0 for i in range(max)]
            pass


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
