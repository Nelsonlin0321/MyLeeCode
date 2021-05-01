#https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
#Runtime: 12 ms, faster than 94.65% of Python online submissions for Binary Tree Preorder Traversal.
#Memory Usage: 13.5 MB, less than 47.06% of Python online submissions for Binary Tree Preorder Traversal.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.order_list = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.order_list.append(root.val)
        self.add_node(root)
        return self.order_list
    def add_node(self,root):
        if root.left is not None:
            self.order_list.append(root.left.val)
            self.add_node(root.left)
        if root.right is not None:
            self.order_list.append(root.right.val)
            self.add_node(root.right)