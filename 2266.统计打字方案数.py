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
        countList = []
        current = pressedKeys[0]
        count = 0
        for i in pressedKeys:
            if i == current:
                count += 1
            else:
                countList.append(
                    [count, 4 if current == '7' or current == '9' else 3])
                current = i
                count = 1
        countList.append([count, 4 if current == '7' or current == '9' else 3])
        res = 1
        print(countList)
        for g in countList:
            res = res * self.getPossibility(g[0], g[1]) % 1000000007
        return res

    def getPossibility(self, length, max):
        try:
            return self.posMap[max][length]
        except:
            log = [0 for i in range(max+1)]
            for i in range(1, length+1):
                if i == 1:
                    log[0] = 1
                    log[1] = 1
                else:
                    for j in reversed(range(1, max+1)):
                        log[j] = log[j-1]
                    log[0] = sum(log[1:])
            total = log[0]
            self.posMap[max][length] = total
            return total


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # print(s.getPossibility(36, 3))
    print(s.countTexts('22233'))
    print(s.countTexts('222222222222222222222222222222222222'))
    print(s.countTexts('55555555999977779555'))
