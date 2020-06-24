# Author: Abdulrahman Jouhari
# Date: June 24, 2020
# Project: Convert Binary Number in a Linked List to Integer

# Instructions: Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Example: 
# Input: head = [1,0,1]
# Output: 5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_nums = []
        binary_counter = 1
        answer = 0
        while head:
            binary_nums.append(head.val)
            head = head.next
        for i in range(len(binary_nums)):
            j = binary_nums.pop()
            if j == 1:
                answer += binary_counter
            binary_counter *= 2
        return answer