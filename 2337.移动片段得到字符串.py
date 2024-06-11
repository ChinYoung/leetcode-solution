#
# @lc app=leetcode.cn id=2337 lang=python3
#
# [2337] 移动片段得到字符串
#

# @lc code=start
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        max_idx = len(target) - 1
        while t_pointer <= max_idx and s_pointer <= max_idx:
            if target[t_pointer] == '_':
                t_pointer += 1
                continue
            if target[t_pointer] == 'L':
                if start[s_pointer] == '_':
                    s_pointer += 1
                    continue
                if start[s_pointer] == 'L':
                    if s_pointer < t_pointer:
                        # print(1)
                        return False
                    s_pointer += 1
                    t_pointer += 1
                    continue
                if start[s_pointer] == 'R':
                    # print(2)
                    return False
            if target[t_pointer] == 'R':
                if start[s_pointer] == '_':
                    s_pointer += 1
                    continue
                if start[s_pointer] == 'R':
                    if s_pointer > t_pointer:
                        # print(3)
                        return False
                    s_pointer += 1
                    t_pointer += 1
                    continue
                if start[s_pointer] == 'L':
                    # print(4)
                    return False
        while s_pointer <= max_idx:
            if start[s_pointer] != '_':
                # print(5)
                return False
            s_pointer += 1
        while t_pointer <= max_idx:
            if target[t_pointer] != '_':
                # print(6)
                return False
            t_pointer += 1
        return True
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    start = '_L__R__R_'
    target = 'L______RR'
    print(s.canChange(start, target))