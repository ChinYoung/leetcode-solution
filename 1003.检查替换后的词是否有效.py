#
# @lc app=leetcode.cn id=1003 lang=python3
#
# [1003] 检查替换后的词是否有效
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        cur = s
        prev = s
        while True:
            prev = cur
            cur = self.removeAbc(prev)
            if cur == prev:
                return len(cur) == 0

    def removeAbc(self, string):
        temp = ''
        expect = 'a'
        res = ''
        for i in string:
            if i == expect:
                # there is a 'abc', discard and restart
                if expect == 'c':
                    temp = ''
                else:
                    temp += i
                # set new expectation char
                if i == 'a':
                    expect = 'b'
                elif i == 'b':
                    expect = 'c'
                elif i == 'c':
                    expect = 'a'
            else:
                # not a valid 'abc', save latest char to the return value
                res += temp
                # a fresh new start with char 'a'
                if i == 'a':
                    expect = 'b'
                    temp = i
                else:
                    # not a fresh start, save the current char to the return value
                    res += i
                    temp = ''
                    expect = 'a'
        res += temp
        return res
        

# @lc code=end

if __name__ == '__main__':

    s = Solution()
    print(s.isValid('abcabcababcc'))
    print(s.isValid('abccba'))
    print(s.isValid('aabcbc'))
