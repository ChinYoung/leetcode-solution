#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#

# @lc code=start
import math
from typing import List, Dict
import time


class SolutionB:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        res = 0
        logMap = self.getLogMap(n, group, profit)
        # print(logMap)
        for costMap in logMap.values():
            for totalProfit, count in costMap.items():
                if totalProfit >= minProfit:
                    res += count
        return res + (1 if minProfit == 0 else 0)

    def getLogMap(self, maxCost: int, costList:List[int], profitList:List[int])-> Dict[str, Dict[str, int]]:
        if len(costList) == 1:
            return {costList[0]: {profitList[0]:1}}
        nextMap = self.getLogMap(maxCost, costList[1:], profitList[1:])
        thisCost = costList[0]
        thisProfit = profitList[0]
        newMap = {}
        for cost, costMap in nextMap.items():
            if cost > maxCost:
                continue
            newMap[cost] = newMap.setdefault(cost, {})
            for profit, count in costMap.items():
                newMap[cost][profit] = count
        for cost, costMap in nextMap.items():
            if cost > maxCost:
                continue
            for profit, count in costMap.items():
                if cost + thisCost > maxCost:
                    continue
                newMap[cost + thisCost] = newMap.setdefault(cost + thisCost, {})
                try:
                    newMap[cost + thisCost][profit + thisProfit] = costMap[cost + thisCost][profit+thisProfit] + 1
                except:
                    newMap[cost + thisCost][profit + thisProfit] = 1
        if thisCost <= maxCost:
            thisCostMap = newMap.setdefault(thisCost, {})
            thisCostMap[thisProfit] = thisCostMap.setdefault(thisProfit, 0) + 1
        # print(maxCost, thisCost, thisProfit, nextMap, newMap)
        return newMap
                

class SolutionA:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD
        
        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % MOD
# @lc code=end

if __name__ == '__main__':
    sa = SolutionA()
    sb = SolutionB()
    # print(s.profitableSchemes(5, 3, [2, 2], [2, 3]))
    # print(s.profitableSchemes(10, 5, [2, 3,5], [6, 7,8]))
    # print(s.profitableSchemes(1, 1, [2, 2,2,2,2], [1,2,1,1,0]))
    # print(s.profitableSchemes(64, 0, [80, 40], [88, 88]))

    # start = time.time()
    # print(sa.profitableSchemes(
    #     95, 53, 
    #     [82,7,18,34,1,3,83,56,50,34,39,38,76,92,71,2,6,74,1,82,22,73,88,98,6,71,6,26,100,75,57,88,43,16,22,89,7,9,78,97,22,87,34,81,74,56,49,94,87,71,59,6,20,66,64,37,2,42,30,87,73,16,39,87,28,9,95,78,43,59,87,78,2,93,7,22,21,59,68,67,65,63,78,20,82,35,86], 
    #     [45,57,38,64,52,92,31,57,31,52,3,12,93,8,11,60,55,92,42,27,40,10,77,53,8,34,87,39,8,35,28,70,32,97,88,54,82,54,54,10,78,23,82,52,10,49,8,36,9,52,81,26,5,2,30,39,89,62,39,100,67,33,86,22,49,15,94,59,47,41,45,17,99,87,77,48,22,77,82,85,97,66,3,38,49,60,66]
    #     )
    # )
    # print(time.time() - start)
    
    start = time.time()
    print(sb.profitableSchemes(
        95, 53, 
        [82,7,18,34,1,3,83,56,50,34,39,38,76,92,71,2,6,74,1,82,22,73,88,98,6,71,6,26,100,75,57,88,43,16,22,89,7,9,78,97,22,87,34,81,74,56,49,94,87,71,59,6,20,66,64,37,2,42,30,87,73,16,39,87,28,9,95,78,43,59,87,78,2,93,7,22,21,59,68,67,65,63,78,20,82,35,86], 
        [45,57,38,64,52,92,31,57,31,52,3,12,93,8,11,60,55,92,42,27,40,10,77,53,8,34,87,39,8,35,28,70,32,97,88,54,82,54,54,10,78,23,82,52,10,49,8,36,9,52,81,26,5,2,30,39,89,62,39,100,67,33,86,22,49,15,94,59,47,41,45,17,99,87,77,48,22,77,82,85,97,66,3,38,49,60,66]
        )
    )
    print(time.time() - start)


