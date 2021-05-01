#https://leetcode.com/problems/find-bottom-left-tree-value/submissions/
# Runtime: 28 ms, faster than 96.20% of Python online submissions for Find Bottom Left Tree Value.
# Memory Usage: 18.4 MB, less than 18.25% of Python online submissions for Find Bottom Left Tree Value.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.value_list = []
        
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.find_deepest_left(root,0)
        max_deepth = max([ deepth for (deepth,value) in self.value_list])
        return [ value for (deepth,value) in self.value_list if deepth ==max_deepth][0]
        
    def find_deepest_left(self,root,deepth):
        if (root.left is None and root.right is None ):
            self.value_list.append((deepth,root.val)) 
        else:
            if root.left is not None:
                left_deepth = deepth+1
                self.find_deepest_left(root.left,left_deepth)
            if root.right is not None:
                right_deepth = deepth+1
                self.find_deepest_left(root.right,right_deepth)
            
        
            
        