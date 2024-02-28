#
# @lc app=leetcode.cn id=2900 lang=python3
#
# [2900] 最长相邻不相等子序列 I
#

# @lc code=start
from typing import List


class Solution:
    def getLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        start_with_0 = []
        start_with_1 = []
        for i in range(n):
            if len(start_with_0) == 0 and groups[i] == 0:
                start_with_0.append(i)
            if len(start_with_1) == 0 and groups[i] == 1:
                start_with_1.append(i)
            if len(start_with_0) != 0 and groups[start_with_0[-1]] + groups[i] == 1:
                start_with_0.append(i)
            if len(start_with_1) != 0 and groups[start_with_1[-1]] + groups[i] == 1:
                start_with_1.append(i)
        if len(start_with_1) > len(start_with_0):
            return [words[i] for i in start_with_1]
        else:
            return [words[i] for i in start_with_0]

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.getLongestSubsequence(3, ["e","a","b"], [0,0,1]))
    print(s.getLongestSubsequence(4, ["a","b","c","d"], [1,0,1,1]))

