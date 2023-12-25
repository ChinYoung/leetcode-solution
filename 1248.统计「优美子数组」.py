#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#

# @lc code=start
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        evenLog = []
        evenCount = 0
        for i in nums:
            if i % 2 == 1:
                if len(evenLog) == k:
                    eventNumBefore = evenLog[0]
                    evenNumAfter = evenCount
                    total += (eventNumBefore+1)*(evenNumAfter + 1)
                    evenLog.pop(0)
                    evenLog.append(evenCount)
                    evenCount = 0
                else:
                    evenLog.append(evenCount)
                    evenCount = 0
            else:
                evenCount += 1
            # print(evenLog)
        if len(evenLog) == k:
            eventNumBefore = evenLog[0]
            evenNumAfter = evenCount
            total += (eventNumBefore+1)*(evenNumAfter + 1)
        return total

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubarrays([1,1,2,1,1], 3))
    print(s.numberOfSubarrays([1,1,2,2,1,1,1], 3))
    print(s.numberOfSubarrays([2,4,6], 1))
    print(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))

