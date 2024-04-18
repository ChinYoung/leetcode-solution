#
# @lc app=leetcode.cn id=1352 lang=python3
#
# [1352] 最后 K 个数的乘积
#

# @lc code=start
class ProductOfNumbers:

    def __init__(self):
        self.product_list = [1]
        self.boundary = 0
        self.count = 0


    def add(self, num: int) -> None:
        self.count += 1
        if num == 0:
            self.boundary = self.count
            self.product_list = [1]
        else:
            self.product_list.append(num * self.product_list[-1])

    def getProduct(self, k: int) -> int:
        num_count = self.count - self.boundary
        if k > num_count:
            return 0
        return int(self.product_list[-1] / self.product_list[num_count - k])



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end

