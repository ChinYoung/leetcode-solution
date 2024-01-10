#
# @lc app=leetcode.cn id=1954 lang=python3
#
# [1954] 收集足够苹果的最小花园周长
#

# @lc code=start


from math import floor


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        length = 1
        while self.getTotal(length) < neededApples:
            length += 1
        return length * 8

    def getTotal(self, i):
        return 4 * (self.getSum(i-1) * (i+1) + i * self.getSum(i + 1))
        # return 4 * (i * self.getSum(i + 1) + self.getSum(i -1) * (i + 1))
        # return 4 * (self.getSum(i-1)*(2 * i + 1) + 2 * i * i + 3 * i)

    def getSum(self, max):
        if max == 1:
            return 1
        if max % 2 != 0:
            return int((0.5 * max) * (max + 1))
        return int((max + 1) * (0.5 * max))
# @lc code=end

if __name__ =="__main__":
    s =Solution()
    print(s.minimumPerimeter(1))
    print(s.minimumPerimeter(13))
    print(s.minimumPerimeter(1000000000))
    print(s.minimumPerimeter(2784381467700))
    # print(s.minimumPerimeter(13))
    # print(s.getTotal(3))
    # print(s.getTotal(2))
    # print(s.getTotal(1))
    # print(s.getSum(1))
    # print(s.getSum(2))
    # print(s.getSum(3))
    # print(s.getSum(6))
    # print(s.getSum(7))

