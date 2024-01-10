#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.getValidIp(s, 4)

    def getValidIp(self, s: str, count: int):
        if count == 1:
            if (len(s) ==0) or (len(s) >1 and s.startswith('0')) or int(s) > 255:
                return[]
            return [s]
        pointer = 0
        ipStr = ''
        validCombinations = []
        maxIndex = len(s) - 1
        while pointer <=maxIndex:
            ipStr = ipStr + s[pointer]
            if len(ipStr)>1 and ipStr.startswith('0'):
                break
            if int(ipStr) <=255:
                validCombinations.append([ipStr, s[pointer+1:]])
                pointer += 1
            else:
                break
        result = []
        for combination in validCombinations:
            currentStr = combination[0]
            restStr = combination[1]
            restStrResult = self.getValidIp(restStr, count -1)
            if len(restStrResult) > 0:
                for restStr in restStrResult:
                    result.append('{}.{}'.format(currentStr, restStr))
        return result

# @lc code=end

if __name__ =='__main__':
    s = Solution()
    print(s.restoreIpAddresses('25525511135'))
    print(s.restoreIpAddresses("0000"))
    print(s.restoreIpAddresses("101023"))

