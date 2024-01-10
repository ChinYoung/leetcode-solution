#
# @lc app=leetcode.cn id=1488 lang=python3
#
# [1488] 避免洪水泛滥
#

# @lc code=start
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = []
        resolveDayIndexList = []
        rainMap = {}
        for idx, i in enumerate(rains):
            if i > 0:
                pastRainIndex = rainMap.setdefault(i, -1)
                # print(resolveDayIndexList,i, pastRainIndex)
                if pastRainIndex != -1:
                    if len(resolveDayIndexList) == 0:
                        return []
                    else:
                        resolveDayIndex = -1
                        for rIndex, r in enumerate(resolveDayIndexList):
                            if r > pastRainIndex:
                                resolveDayIndex = resolveDayIndexList.pop(rIndex)
                                break
                        if resolveDayIndex == -1:
                            return []
                        res[resolveDayIndex] = i
                res.append(-1)
                rainMap[i] = idx
            else:
                resolveDayIndexList.append(idx)
                res.append(1)
        return res



# @lc code=end
    
if __name__ =="__main__":
    s = Solution()
    # print(s.avoidFlood([0,1,1]))
    # print(s.avoidFlood([1,2,3,4]))
    # print(s.avoidFlood([1,2,0,0,2,1]))
    # print(s.avoidFlood([1,2,0,1,2]))
    # print(s.avoidFlood([69,0,0,0,69]))
    # print(s.avoidFlood([1,0,2,0,2,1]))
    # print(s.avoidFlood([3,5,4,0,1,0,1,5,2,8,9]))
    # print(s.avoidFlood([1,3,2,0,2,0,3,0,1,0,0,0]))
    print(s.avoidFlood([3,0,0,1,2,0,0,1,3,2]))

