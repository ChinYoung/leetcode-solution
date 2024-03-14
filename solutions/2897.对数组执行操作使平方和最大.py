#
# @lc app=leetcode.cn id=2897 lang=python3
#
# [2897] 对数组执行操作使平方和最大
#

# @lc code=start
from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bits = [0] * 32
        mod = int(1e9 + 7)
        for num in nums:
            for i in range(32):
                if num & 1<<i:
                    bits[i] += 1
        res = 0
        for _ in range(k):
            n = 0
            for j in range(32):
                if bits[j] > 0:
                    bits[j] -= 1
                    n += 1<<j
            res += n * n
        return res % mod

# notes:
# 1. 获取比特位计算值使用位运算速度快        1 << 3  == str('1000', 2)
# 2. 检查比特位值时, 使用比特运算符快且方便   
#       a = 8  
#       二进制0b00001000  
#       检查第三位是否是1   
#       a & 1<<3


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    num_list = [2,6,5,8]
    k = 2
    print(s.maxSum(num_list, k))
    num_list = [4,5,4,7]
    k = 3
    print(s.maxSum(num_list, k))