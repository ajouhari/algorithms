# Author: Abdulrahman Jouhari
# Date: June 24, 2020
# Project: XOR Operation in an Array

# Instructions: Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

# Example: 
# Input: n = 5, start = 0
# Output: 8

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [(start + 2*i) for i in range(n)]
        answer = nums[0]
        for i in nums[1:]:
            answer = answer ^ i
        return answer