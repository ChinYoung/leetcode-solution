#
# @lc app=leetcode.cn id=2136 lang=python3
#
# [2136] 全部开花的最早一天
#

# @lc code=start


from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        sortedPairs = sorted(zip(plantTime, growTime), key =lambda pair:(pair[1], -1 * pair[0]), reverse=True)
        pastTime = 0
        res = 0
        for pair in sortedPairs:
            plantTimeValue = pair[0]
            growTimeValue = pair[1]
            pastTime += plantTimeValue
            res = max(pastTime + growTimeValue, res)
        return res

# @lc code=end

if __name__ =="__main__":
    s = Solution()
    print(s.earliestFullBloom([1,2,3,2], [2,1,2,1]))
    print(s.earliestFullBloom([1,4,3], [2,3,1]))
    print(s.earliestFullBloom([1], [1]))