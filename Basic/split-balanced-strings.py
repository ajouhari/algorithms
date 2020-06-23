# Author: Abdulrahman Jouhari
# Project: Split a String in Balanced Strings

# Instructions: Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_r = 0
        num_l = 0
        counter = 0
        for i in range(len(s)):
            if s[i] == 'R':
                num_r += 1
            else:
                num_l += 1
            if num_r == num_l:
                counter += 1
        return counter