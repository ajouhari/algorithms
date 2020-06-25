# Author: Abdulrahman Jouhari
# Date: June 25, 2020
# Project: To Lower Case

# Instructions: Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example:
# Input: "Hello"
# Output: "hello"

# toLowerCase() is built in, here is the function
class Solution:
    def toLowerCase(self, str: str) -> str:
        for i in range(len(str)):
            if ord(str[i]) >= 65 and ord(str[i]) <= 90:
                letter = chr(ord(str[i]) + 32)
                str = str[:i] + letter + str[i + 1:]
        return str