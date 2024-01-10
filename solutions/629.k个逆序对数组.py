#
# @lc app=leetcode.cn id=629 lang=python3
#
# [629] K个逆序对数组
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.log = {}
    
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        if n == 1:
            return 0
        try:
            res = self.log[n][k]
            return res
        except KeyError:
            # f(n, k) = f(n-1, k) + f(n-1, k-1) + f(n-1, k-2) + ..... + f(n-1, k-n+1)
            # f(n, k+1) = f(n-1, k+1) + f(n-1, k) + f(n-1, k-1) + ..... + f(n-1, k+1-n+1)
            # =>
            # f(n, k+1) - f(n,k) = f(n-1, k+1) - f(n-1, k-n+1)
            # =>
            # f(n, k+1) = f(n,k) + f(n-1, k+1) - f(n-1, k-n+1)
            # =>
            # f(n, k) = f(n,k-1) + f(n-1, k) - f(n-1, k-n)
            a = self.kInversePairs(n, k-1)
            b = self.kInversePairs(n-1, k)
            c = self.kInversePairs(n-1, k-n) if k>n-1 else 0
            # print(a,b,c)
            count = a+b-c
            nLog = self.log.setdefault(n, {})
            nLog[k] = count
            return count % (pow(10,9) + 7)

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.kInversePairs(2,2))
    print(s.kInversePairs(3,0))
    print(s.kInversePairs(3,1))
    print(s.kInversePairs(4,2))

