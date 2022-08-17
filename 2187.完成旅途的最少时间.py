#
# @lc app=leetcode.cn id=2187 lang=python3
#
# [2187] 完成旅途的最少时间
#

# @lc code=start
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        sortedTime = sorted(time)
        maxTripLength = totalTrips * sortedTime[-1]
        start = 1
        end = maxTripLength
        while end > start:
            mid = start + 0.5 * (end - start)
            trips = self.getTrips(sortedTime, mid)
            if trips >= totalTrips:
                end = mid
            else:
                start += 1
        return start

    def getTrips(self, time, currentTime):
        final = 0
        for i in time:
            if i <= currentTime:
                final += (currentTime // i)
            else:
                break
        return final

# @lc code=end

if __name__ =="__main__":
    s = Solution()
    print(s.minimumTime([5,10,10], 9))

