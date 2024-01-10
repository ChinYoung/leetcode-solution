#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
from functools import reduce
from hashlib import new


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        lefts = [[s1, s2]]
        temp = ''
        for i in s3:
            temp += i
            if len(lefts) == 0:
                return False
            newLeft = []
            newPairMap = {}
            for l in lefts:
                leftS1 = l[0]
                leftS2 = l[1]
                if temp == s3 and ((leftS1 == '' and leftS2 == i) or (leftS2 == '' and leftS1 == i)):
                    return True
                if len(leftS1) > 0 and leftS1[0] == i:
                    newS1 = leftS1[1:]
                    newS2 = leftS2
                    key = '{},{}'.format(newS1, newS2)
                    if not newPairMap.setdefault(key, False):
                        newLeft.append([newS1, newS2])
                        newPairMap[key] = True
                if len(leftS2) > 0 and leftS2[0] == i:
                    newS1 = leftS1
                    newS2 = leftS2[1:]
                    key = '{},{}'.format(newS1, newS2)
                    if not newPairMap.setdefault(key, False):
                        newLeft.append([newS1, newS2])
                        newPairMap[key] = True
            # print(temp, newLeft)
            newPairMap = {}
            lefts = newLeft
        return len(lefts) > 0 and reduce(lambda final, cur: final and (cur == ['', '']), lefts, True)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
    print(s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
    print(s.isInterleave('', '', ''))
    print(s.isInterleave('a', '', 'a'))
    print(s.isInterleave('', '', 'a'))
    print(s.isInterleave('a', '', 'c'))
    print(s.isInterleave('abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb', 'ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc',
          'cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc'))
