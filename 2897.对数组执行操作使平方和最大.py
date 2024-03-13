#
# @lc app=leetcode.cn id=2897 lang=python3
#
# [2897] 对数组执行操作使平方和最大
#

# @lc code=start
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        
        pass

    def group(self, nums: List[int]):
        res = []
        for i in range(34):
            number = int(''.join([str(s) for s in [1 if j == 0 else 0 for j in range(i)]]), 2)

    def getNumberByPosition(self, length: int):
        
        return int(''.join([str(s) for s in [1 if j == 0 else 0 for j in range(length)]]), 2)


    def getBest(self, number: int) -> int:
        string = bin(number).replace('0b', '')
        length = len(string)
        best = []
        for i in string:
            best += ('1' if i == '0' else '0')
        return int(best, 2)

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.getBest(9))

