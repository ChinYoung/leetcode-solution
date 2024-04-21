#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        if p == '*':
            return True
        slice_list = self.split(p)
        if len(slice_list) == 1:
            if len(s) != len(p):
                return False
            for i in range(len(s)):
                if not (s[i] == p[i] or p[i] == '?'):
                    return False
            return True
        left = s
        if slice_list[0] != '*':
            # 检查头能不能匹配能不能匹配
            sl = slice_list.pop(0)
            if len(sl) > len(left):
                return False
            s_slice = left[:len(sl)]
            left = left[len(sl):]
            for i in range(len(sl)):
                if not (sl[i] == s_slice[i] or sl[i] == '?'):
                    return False
        if slice_list[-1] != '*':
            # 检查尾巴能不能匹配
            sl = slice_list.pop()
            if len(sl) > len(left):
                return False
            s_slice = left[len(left)-len(sl):]
            left = left[:len(left) - len(sl)]
            for i in range(len(sl)):
                if not (sl[-1 - i] == s_slice[-1-i] or sl[-1 - i] == '?'):
                    return False
        # 头尾可以匹配, 检查p中剩余的非*部分是否是s剩余部分的子序列
        s_max_index = len(left) - 1
        s_pointer = 0
        p_pointer = 0
        for sl in slice_list:
            if sl == '*':
                continue
            else:
                max_index = len(sl) - 1
                s_pointer_bak = s_pointer
                while p_pointer <= max_index:
                    # s指针到队尾也无法找到与p切片匹配的字符串
                    if s_pointer > s_max_index:
                        return False
                    if left[s_pointer] == sl[p_pointer] or sl[p_pointer] == '?':
                        s_pointer += 1
                        p_pointer += 1
                    else:
                        # 遇到不匹配的, s的初始指针前进一位, p的切片从头开始, 再次尝试匹配, 
                        s_pointer = s_pointer_bak + 1
                        p_pointer = 0
                        s_pointer_bak = s_pointer
                p_pointer = 0
        return True

    def split(self, s: str):
        res = []
        temp = ''
        for i in s:
            if i == '*':
                if temp != '':
                    res.append(temp)
                    temp = ''
                res.append(i)
            else:
                temp += i
        if temp != '':
            res.append(temp)
        return res

# @lc code=end

if __name__ =="__main__":
    s = Solution()
    # string = "cb"
    # pattern = "?a"
    # print(s.isMatch(string, pattern))
    # string = "aa"
    # pattern = "*"
    # print(s.isMatch(string, pattern))

    # string = "aaaaaababaa"
    # pattern = "a*ba*b*"
    # print(s.isMatch(string, pattern))
    # string = "abcabczzzde"
    # pattern = "*abc???de*"
    # print(s.isMatch(string, pattern))
    # string = "hi"
    # pattern = "*?"
    # print(s.isMatch(string, pattern))
    # string = "aaab"
    # pattern = "b**"
    # print(s.isMatch(string, pattern))
    # string = "mississippi"
    # pattern = "m??*ss*?i*pi"
    # print(s.isMatch(string, pattern))
    # string = "b"
    # pattern = "?*?"
    # print(s.isMatch(string, pattern))
    string = "ab"
    pattern = "*ab"
    print(s.isMatch(string, pattern))
