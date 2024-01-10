#
# @lc app=leetcode.cn id=1807 lang=python3
#
# [1807] 替换字符串中的括号内容
#

# @lc code=start
from functools import reduce
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        idx = 0
        maxIndex = len(s) - 1
        current = ''
        isInBracket = False
        res = ''
        def toMap(final, current):
            final = final if final else {}
            key = current[0]
            value = current[1]
            final[key] = value
            return final
        valueMap = reduce(toMap, knowledge, {})
        while idx <= maxIndex:
            currentChar = s[idx]
            idx += 1
            if currentChar == '(':
                isInBracket = True
                continue
            if currentChar == ')':
                isInBracket = False
                try:
                    valueOfKey = valueMap[current]
                    res += valueOfKey
                except KeyError:
                    res += '?'
                current = ''
                continue
            if isInBracket:
                current += currentChar
            else:
                res += currentChar
        return res
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.evaluate('hi(name)', [["a","b"]]))
    print(s.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]))
    print(s.evaluate("(a)(a)(a)aaa", [["a","yes"]]))

