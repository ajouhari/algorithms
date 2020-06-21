class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_total = 0
        total = []
        for i in nums:
            running_total += i
            total.append(running_total)
        return total