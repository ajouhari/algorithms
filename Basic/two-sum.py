# Author: Abdulrahman Jouhari
# Project: Two Sum 

# Instructions: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            compliment = target - number
            if compliment not in seen:
                seen[number] = i
            else:
                return [seen[compliment], i]