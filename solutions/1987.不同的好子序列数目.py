#
# @lc app=leetcode.cn id=1987 lang=python3
#
# [1987] 不同的好子序列数目
#

# @lc code=start
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        end_with_0 = 0
        end_with_1 = 0
        mod = 1e9 + 7
        z_num = 0
        for i in binary:
            if i == '0':
                end_with_0 = (end_with_0 + end_with_1) % mod
                z_num = 1
            else:
                end_with_1 = (end_with_1 + 1 + end_with_0) % mod
        return int((end_with_0 + end_with_1 + z_num) % mod)

# @lc code=end


if __name__ =='__main__':
    s = Solution()
    # print(s.countSubSeq(4))
    print(s.numberOfUniqueGoodSubsequences('001'))
    print(s.numberOfUniqueGoodSubsequences('11'))
    print(s.numberOfUniqueGoodSubsequences('101'))