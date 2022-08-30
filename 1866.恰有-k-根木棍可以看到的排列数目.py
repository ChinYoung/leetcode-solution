#
# @lc app=leetcode.cn id=1866 lang=python3
#
# [1866] 恰有 K 根木棍可以看到的排列数目
#

# @lc code=start






class Solution:
    def __init__(self) -> None:
        self.log = {}
        self.factorialLog = {}
        self.possibilityLog = {}

    def rearrangeSticksX(self, n: int, k: int) -> int:
        mod = 10**9+7
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = (dp[i-1][j-1]+((i-1)*dp[i-1][j]))
        return dp[n][k]


    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 1000000007
        row = self.log.setdefault(n, {})
        try:
            return row[k]
        except KeyError:
            if n == k:
                row[k] = 1
                return 1
            if n < k:
                row[k] = 0
                return 0
            if k == 1:
                result = (self.getFactorial(n-1))
                row[k] = result
                return result
            total = 0
            selected = 1
            while (n - selected) >= (k -1):
                total += (self.getPossibilities(n, selected) * self.rearrangeSticks(n-selected, k-1))
                selected += 1
            result = total
            row[k] = result
            return result

    def getFactorial(self, n):
        try:
            return self.factorialLog[n]
        except KeyError:
            result = 1
            f = n
            while f > 0:
                result *= f
                f -= 1
            self.factorialLog[n] = result
            return result

    def getPossibilities(self,n:int, selected:int):
        if selected == 1:
            return 1
        row = self.possibilityLog.setdefault(n, {})
        try:
            return row[selected]
        except KeyError:
            result = int(self.getFactorial(n-1) / self.getFactorial(n-selected))
            row[selected] = result
            return result
# @lc code=end

# def getPossibilities(self, length:int):
#     if length == 1:
#         return 1
#     next = self.getPossibilities(length- 1)
#     return length + (length-1)*(next -1)

if __name__ == "__main__":
    s = Solution()
    # print(s.getPossibilities(4, 2))
    print(s.rearrangeSticksX(29,12))
    print(s.rearrangeSticks(29,12))
