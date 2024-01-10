#
# @lc app=leetcode.cn id=2187 lang=python3
#
# [2187] 完成旅途的最少时间
#

# @lc code=start
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        maxTripLength = totalTrips * max(time)
        start = 1
        end = maxTripLength
        while end > start:
            length = end - start
            mid = start +  length // 2
            if self.verifyMid(time, mid, totalTrips):
                end = mid
            else:
                start = mid+1
        return start

    def verifyMid(self, time, currentTime, totalTrips):
        final = 0
        for i in time:
            if i <= currentTime:
                final += (currentTime // i)
        return final >= totalTrips

# @lc code=end

if __name__ =="__main__":
    s = Solution()
    print(s.minimumTime([5,10,10], 9))
    print(s.minimumTime([1,2,3], 5))

