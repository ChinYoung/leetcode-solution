#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        numMap = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "a": -1,
            "b": -1,
            "c": -1,
            "d": -1,
            "e": -1,
            "f": -1,
            "g": -1,
            "h": -1,
            "i": -1,
            "j": -1,
            "k": -1,
            "l": -1,
            "m": -1,
            "n": -1,
            "o": -1,
            "p": -1,
            "q": -1,
            "r": -1,
            "s": -1,
            "t": -1,
            "u": -1,
            "v": -1,
            "w": -1,
            "x": -1,
            "y": -1,
            "z": -1,
        }
        max = -1
        second = -1
        for i in s:
            num = numMap[i]
            if num == max:
                continue
            if num > max:
                second = max
                max = num
                continue
            if num > second:
                second = num
        return second
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.secondHighest('dfa12321afd'))
    print(s.secondHighest('abc1111'))
    print(s.secondHighest('sjhtz8344'))
