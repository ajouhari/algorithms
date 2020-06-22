class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = str(n)
        product_1 = 1
        sum_1 = 0
        for i in range(len(x)):
            product_1 *= int(x[i])
            sum_1 += int(x[i])
        return product_1 - sum_1