#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        maxStr = s[0]
        for i in range(len(s)):
            try:
                center=self.isCenterEven(s, i)
                left = center[0]
                right = center[1]
                expanded = self.expand(s, left, right)
                expandedLength = len(expanded)
                if expandedLength > maxLength:
                    maxStr = expanded
                    maxLength = expandedLength
            except Exception:
                pass
            try:
                center=self.isCenterOdd(s, i)
                left = center[0]
                right = center[1]
                expanded = self.expand(s, left, right)
                expandedLength = len(expanded)
                if expandedLength > maxLength:
                    maxStr = expanded
                    maxLength = expandedLength
            except Exception:
                pass
        return maxStr

    def expand(self, s:str, left:int, right:int):
        maxIndex = len(s)-1
        result = s[right-1] if (right-left)>1 else ""
        print(left,right, result, '=========')
        if left>=0 and right<=maxIndex:
            leftChar = s[left]
            while left>=0 and right<=maxIndex and leftChar == s[right]:
                result = leftChar + result + leftChar
                left-=1
                right+=1
                leftChar = s[left]
        return result

    def isCenterEven(self, s:str, index:int):
        if index-1>=0 and s[index] == s[index -1]:
            return [index-1, index]
        raise Exception('not a center')

    def isCenterOdd(self, s:str, index:int):
        if index-1>=0 and index+1<= len(s)-1 and s[index-1]==s[index+1]:
            return [index-1, index+1]
        raise Exception('not a center')




# @lc code=end

if __name__ =="__main__":
    s = Solution()
    print(s.longestPalindrome("ccc"))
