# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/
# Runtime: 44 ms, faster than 66.25% of Python online submissions for Kth Smallest Element in a BST.
# Memory Usage: 21.3 MB, less than 38.52% of Python online submissions for Kth Smallest Element in a BST.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution(object):
    def __inti__(self):
        self.heap = []
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        k_val = 0
        self.heap.append(root.val)
        self.add_node(root)
        for _ in range(k):
            k_val = heapq.heappop(self.heap)
        return k_val
        
    def add_node(self,root):
        if root.left is not None:
            heapq.heappush(self.heap,root.left.val)
            self.add_node(root.left)
        if root.right is not None:
            heapq.heappush(self.heap,root.right.val)
            self.add_node(root.right)