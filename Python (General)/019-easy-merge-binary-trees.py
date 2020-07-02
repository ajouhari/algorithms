# Author: Abdulrahman Jouhari
# Date: June 26, 2020
# Project: Merge Two Binary Trees

# Instructions: Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not. You need to merge them into
# a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new
# value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

# Example:
# Input: 
# Tree 1                     Tree 2                  
#           1                         2  
#          / \                       / \   
#         3   2                     1   3   
#        /                           \   \  
#       5                             4   7
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        else:
            t1.val += t2.val
            t1.right = self.mergeTrees(t1.right, t2.right)
            t1.left = self.mergeTrees(t1.left, t2.left)
            return t1
        