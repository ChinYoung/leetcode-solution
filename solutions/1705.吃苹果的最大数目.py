#
# @lc app=leetcode.cn id=1705 lang=python3
#
# [1705] 吃苹果的最大数目
#

# @lc code=start
from typing import List, Dict
import heapq


class Solution:
    def __init__(self) -> None:
        self.existing = []

    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        result = 0
        passedDays = 0
        for index, count in enumerate(apples):
            passedDays = index
            if self.existing:
                self.filterOutdated(passedDays)
            validDays = days[index]
            if count > 0 and validDays > 0:
                self.addNew(count, validDays, passedDays)
            if self.existing:
                self.eatOne()
                result += 1
        while self.existing:
            passedDays += 1
            self.filterOutdated(passedDays)
            if self.existing:
                self.eatOne()
                result += 1
        return result

    def eatOne(self):
        heapq.heapreplace(
            self.existing, (self.existing[0][0], self.existing[0][1]-1))

    def filterOutdated(self, passedDays: int):
        while self.existing and (self.existing[0][0] <= passedDays or self.existing[0][1] <= 0):
            heapq.heappop(self.existing)

    def addNew(self, count, validDays, passedDays):
        endDay = validDays + passedDays
        heapq.heappush(self.existing, (endDay, count))

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]))
    print(s.eatenApples([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]))
    print(s.eatenApples([20000], [20000]))
    print(s.eatenApples([1], [2]))
    print(s.eatenApples([2, 1, 10], [2, 10, 1]))
