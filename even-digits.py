# Author: Abdulrahman Jouhari
# Project: Find Numbers with Even Number of Digits

# Instructions: Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            str_num = str(num)
            if len(str_num) % 2 == 0:
                i += 1
        return i