#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#

from typing import List
import math
# @lc code=start

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.points = points
        total = 0
        lowest = [[self.getLength(0, i), i] for i in list(range(1, len(points)))]
        while len(lowest) !=0:
            minPointIdx = 0
            minDist = math.inf
            for idx, pointInfo in enumerate(lowest):
                dist, point = pointInfo
                if dist < minDist:
                    minDist = dist
                    minPointIdx = idx
            dist, newPoint = lowest.pop(minPointIdx)
            total += minDist
            lowest = [[self.getLength(newPoint, point), point] if dist > self.getLength(newPoint, point) else [dist, point] for dist, point in lowest]
        return total

    def  getLength(self, aIndex: int, bIndex: int) -> int:
        pointA = self.points[aIndex]
        pointB = self.points[bIndex]
        return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
    print(s.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))
    print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
    print(s.minCostConnectPoints([[-14,-14],[-18,5],[18,-10],[18,18],[10,-2]]))
    print(s.minCostConnectPoints([[7,18],[-15,19],[-18,-15],[-7,14],[4,1],[-6,3]]))

