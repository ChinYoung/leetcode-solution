#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.parseString(s) == self.parseString(t)

    def parseString(self, string):
        parsed = []
        recorder = {}
        counter = 0
        for lt in list(string):
            parsed_value = recorder.get(lt)
            if parsed_value == None:
                parsed_value = counter
                recorder[lt] = counter
                counter = counter + 1
            parsed.append(str(parsed_value))
        return ''.join(parsed)
# @lc code=end

