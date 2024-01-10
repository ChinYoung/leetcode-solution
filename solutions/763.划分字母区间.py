#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        subStrLenList = []
        headChar = s[0]
        tempMax = self.findMax(s, headChar)
        if tempMax == -1:
            subStrLenList.append(1)
            subStrLenList.extend(self.partitionLabels(s[1:]))
        else:
            indexList = [tempMax]
            indexMap = {}
            for i  in s[1:tempMax]:
                iMax = self.findMax(s,i)
                indexList.append(iMax)
                indexMap[i] = iMax
            finalMax = max(indexList)
            while tempMax != finalMax:
                temp = tempMax
                tempMax = finalMax
                newIndexList = []
                for i in s[temp + 1:tempMax + 1]:
                    try:
                        iMax = indexMap[i]
                        newIndexList.append(iMax)
                    except KeyError:
                        iMax = self.findMax(s, i)
                        indexMap[i] = iMax
                        newIndexList.append(iMax)
                finalMax = max(newIndexList)
            if finalMax == (len(s) - 1):
                subStrLenList.append(len(s))
                return subStrLenList
            subStrLenList.append(finalMax + 1)
            subStrLenList.extend(self.partitionLabels(s[finalMax + 1:]))
        return subStrLenList

    def findMax(self, s:str, c:str):
        maxIndex = -1
        for index, i in enumerate(s):
            if i == c and index >= maxIndex:
                maxIndex = index
        return maxIndex



# @lc code=end

if __name__ =="__main__":
    s = Solution()
    print(len("qiejxqfnqceocmy"))
    print(s.partitionLabels("qiejxqfnqceocmy"))

