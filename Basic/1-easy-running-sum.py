# Author: Abdulrahman Jouhari
# Date: June 19, 2020
# Project: Running Sum of 1d Array

# Instructions: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_total = 0
        total = []
        for i in nums:
            running_total += i
            total.append(running_total)
        return total