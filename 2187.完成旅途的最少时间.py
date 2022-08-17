#
# @lc app=leetcode.cn id=2187 lang=python3
#
# [2187] 完成旅途的最少时间
#

# @lc code=start
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if len(time) == 1:
            if time[0] > totalTrips:
                return time[0]
            else:
                factor = 2
                while factor * time[0] < totalTrips:
                    factor += 1
                return (factor-1) * time[0]
        sortedList = sorted(time)
        index = 0
        maxIndex = len(time) - 1
        maxValue = sortedList[index]
        while index <= maxIndex:
            choice = sortedList[:index+1]
            # print(choice)
            if self.getMaxTotal(choice, maxValue) >= totalTrips:
                return maxValue
            nextMaxValue = self.getMavValue(choice)
            if nextMaxValue == maxValue:
                index += 1
                maxValue = sortedList[index]
            else:
                maxValue = nextMaxValue
            # print('nextMax', maxValue)

    def getMavValue(self, time):
        max = time[-1]
        for i in time[:-1]:
            if 2 * i > max:
                return 2 * i
        return max

    def getMaxTotal(self, time:List[int], maxValue:int):
        all = []
        for i in time:
            factor = 2
            while i * factor <= maxValue:
                factor += 1
            all.append(i * (factor-1))
        total = sum(all)
        # print(total)
        return total


# @lc code=end

if __name__ =="__main__":
    s = Solution()
    # print(s.getMaxTotal([1,2,3], 3))
    print(s.minimumTime([1,2,3,7], 9))

