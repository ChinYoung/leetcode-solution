#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] 一手顺子
#

# @lc code=start
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        maxValue = max(hand)
        counter = {}
        # counter = [0]*(maxValue+1)
        for i in hand:
            counter[i] = counter.setdefault(i, 0) + 1
        for i in sorted(counter):
            # print(counter)
            if counter[i] < 0:
                return False
            if counter[i] == 0:
                continue
            while counter[i] > 0:
                try:
                    for j in range(groupSize):
                        counter[i+j] -= 1
                except KeyError:
                    return False
        return True
# @lc code=end


if __name__ =="__main__":
    s = Solution()
    print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
    print(s.isNStraightHand([1,2,3,4,5], 4))
