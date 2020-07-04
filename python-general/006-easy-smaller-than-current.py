# Author: Abdulrahman Jouhari
# Date: June 21, 2020
# Project: How Many Numbers Are Smaller Than the Current Number

# Instructions: Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller = sorted(nums)
        return [smaller.index(i) for i in nums]