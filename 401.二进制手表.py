#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        results = []
        for num in range(turnedOn+1):
            for i in self.getCombinations([1,2,4,8], num):
                for j in self.getCombinations([1,2,4,8,16,32], turnedOn - num):
                    hour = i
                    minute = j
                    if minute < 60 and hour < 12:
                        minuteStr = '0{}'.format(minute) if minute < 10 else '{}'.format(minute)
                        results.append('{}:{}'.format(hour, minuteStr))
        return results

    def getCombinations(self, options: List[int], turnedOn: int):
        if turnedOn == 0:
            return [0]
        if turnedOn == 1:
            return options

        combinations = []
        for i in options:
            clone = options.copy()
            clone.remove(i)
            combinations.append([i, clone])
        current = 1
        while current < turnedOn:
            newCombinations = []
            log = {}
            for i in combinations:
                total = i[0]
                rest: List[int] = i[1]
                for j in rest:
                    newTotal = total + j
                    if not log.setdefault(newTotal, False):
                        jClone = rest.copy()
                        jClone.remove(j)
                        log[newTotal] = True
                        newCombinations.append([newTotal, jClone ])
            combinations = newCombinations
            current += 1
        return map(lambda x:x[0], combinations)

    def countMinute(self, tunedOn:int):
        pass
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.readBinaryWatch(2))