# Author: Abdulrahman Jouhari
# Date: June 25, 2020
# Project: Minimum Time Visiting All Points

# Instructions: On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.
# You can move according to the next rules:
# * In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
# * You have to visit the points in the same order as they appear in the array.

# Example:
# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7

class Solution:     
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps = 0
        for i in range(len(points) - 1):
            point1 = points[i]
            point2 = points[i + 1]
            x = abs(point2[0] - point1[0])
            y = abs(point2[1] - point1[1])
            if abs(x) > abs(y):
                steps += abs(x)
            elif abs(y) > abs(x):
                steps += abs(y)
            else:
                steps += abs(x)
        return steps   