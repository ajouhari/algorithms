# Author: Abdulrahman Jouhari
# Project: Decompress Run-Length Encoded List

# Instructions: We are given a list nums of integers representing a list compressed with run-length encoding.
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
# For each such pair, there are freq elements with value val concatenated in a sublist.
# Concatenate all the sublists from left to right to generate the decompressed list.
# Return the decompressed list.

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        count = 0
        arr = []
        for i in range(len(nums)//2):
            f = nums[count]
            v = nums[(count)+1]
            arr = arr + ([v] * f)
            count +=2
        return arr