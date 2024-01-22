#
# @lc app=leetcode.cn id=2947 lang=python3
#
# [2947] 统计美丽子字符串 I
#

# @lc code=start
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        count_log = []
        total = 0
        for i in s:
            count_log.append([0, 0])
            for p in count_log:
                if self.isVowel(i):
                    p[0] += 1
                else:
                    p[1] += 1
                # print(p, self.isBeautiful(p[0], p[1], k))
                if self.isBeautiful(p[0], p[1], k):
                    total += 1
        return total

    def isVowel(self, c: str):
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

    def isBeautiful(self, vowelCount: int, noneVowelCount:int, k: int) -> bool:
        return vowelCount == noneVowelCount and ((vowelCount * noneVowelCount) % k == 0)
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.beautifulSubstrings('baeyh', 2))
    print(s.beautifulSubstrings('abba', 1))

