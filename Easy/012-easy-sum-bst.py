# Author: Abdulrahman Jouhari
# Date: June 24, 2020
# Project: Range Sum of BST

# Instructions: Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.

# Example: 
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        else:
            return (root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R))