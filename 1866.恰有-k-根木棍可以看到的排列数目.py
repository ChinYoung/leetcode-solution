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

    def rearrangeSticks(self, n: int, k: int) -> int:
        # print(n, k)
        row = self.log.setdefault(n, {})
        try:
            return row[k]
        except KeyError:
            if k == 1:
                if n == 1:
                    row[k] = 1
                    return 1
                else:
                    result = self.getFactorial(n-1)
                    row[k] = result
                    return result
            if n < k:
                row[k] = 0
                return 0
            if n == k:
                row[k] = 1
                return 1
            total = 0
            selected = 1
            while (n - selected) >= (k -1):
                total += (self.getPossibilities(n, selected) * self.rearrangeSticks(n-selected, k-1))
                selected += 1
            row[k] = total
            result = total % (pow(10, 9) + 7)
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
    print(s.rearrangeSticks(3,2))
    print(s.rearrangeSticks(5,5))
    print(s.rearrangeSticks(20,11))
    print(s.rearrangeSticks(105,20))
