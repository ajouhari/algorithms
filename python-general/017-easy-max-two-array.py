# Author: Abdulrahman Jouhari
# Date: June 25, 2020
# Project: Maximum Product of Two Elements in an Array

# Instructions: Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1). 

# Example:
# Input: nums = [3,4,5,2]
# Output: 12 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = max(nums)
        index_to_remove = nums.index(max(nums))
        nums.pop(index_to_remove)
        j = max(nums)
        return (i - 1) * (j - 1)