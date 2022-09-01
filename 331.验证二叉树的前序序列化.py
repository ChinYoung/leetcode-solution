#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start




class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#':
            return True
        if len(preorder) < 5:
            return False
        stack = []
        index = 0
        maxIndex = len(preorder) - 1
        strs = ''
        while index<=maxIndex:
            current = preorder[index]
            if index == maxIndex:
                strs = current
            if current == ',' or index == maxIndex:
                stack.append(strs)
                strs = ''
                # print(stack)
                while len(stack) > 2 and  stack[-1] == '#' and stack[-2] == '#':
                    stack = stack[:-2]
                    if stack[-1] == '#':
                        return False
                    if len(stack) == 1 and index < maxIndex:
                        return False
                    stack[-1] = '#'
            else:
                strs += current
            index += 1
        return len(stack) == 1

# @lc code=end
if __name__ == "__main__":
    s =Solution()
    print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,1,#,#,2,#,#"))
    print(s.isValidSerialization("1,#"))
    print(s.isValidSerialization("9,#,#,1"))
    print(s.isValidSerialization("1,#,#,#,#"))
    print(s.isValidSerialization("#,#,#"))
    print(s.isValidSerialization("9,#,92,#,#"))
