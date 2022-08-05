#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        left_map = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        right_map = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        stack = []
        for letter in s:
            left_value = left_map.get(letter)
            right_value = right_map.get(letter)
            if left_value != None:
                stack.append(letter)
                continue
            if len(stack) !=0 and right_value != None and stack[-1] == right_value:
                stack.pop()
                continue
            return False
        return len(stack) == 0
# @lc code=end

