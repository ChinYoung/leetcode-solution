#
# @lc app=leetcode.cn id=2697 lang=python3
#
# [2697] 字典序最小回文串
#
import math

# @lc code=start
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        head_list = []
        tail_list = []
        str_len = len(s)
        step_to_go = math.floor(str_len/2)
        center_char = '' if str_len % 2 == 0 else s[step_to_go]
        for i in list(range(step_to_go)):
            char_at_head, char_at_tail = s[i], s[str_len - 1 - i]
            char_to_accept = char_at_tail if char_at_head > char_at_tail else char_at_head 
            head_list.append(char_to_accept)
            tail_list.insert(0, char_to_accept)
        return '{}{}{}'.format(''.join(head_list), ''.join([center_char]), ''.join(tail_list))
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.makeSmallestPalindrome('egcfe'))
    print(s.makeSmallestPalindrome('abcd'))
    print(s.makeSmallestPalindrome('axyabby'))