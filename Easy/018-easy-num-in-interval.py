# Author: Abdulrahman Jouhari
# Date: June 25, 2020
# Project: Number of Students Doing Homework at a Given Time

# Instructions: Given two integer arrays startTime and endTime and given an integer queryTime.
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
# Return the number of students doing their homework at time queryTime. More formally,
# return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

# Example:
# Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# Output: 1

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count += 1
        return count