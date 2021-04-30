#https://leetcode.com/problems/balanced-binary-tree/submissions/
#Runtime: 72 ms, faster than 6.98% of Python online submissions for Balanced Binary Tree.
#Memory Usage: 17.7 MB, less than 88.55% of Python online submissions for Balanced Binary Tree.

class Solution(object):
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        left_height = self.find_height(root.left)
        right_height = self.find_height(root.right)
        
        if abs(left_height-right_height)>1:
            return False
        
        left_isBalanced = self.isBalanced(root.left)
        right_isBalanced = self.isBalanced(root.right)
            
        if (not left_isBalanced) or (not right_isBalanced):
            return False 
        
        return True
    
    def find_height(self,root):
        if not root:
            return 0
        return 1+ max(self.find_height(root.left),self.find_height(root.right))

#Runtime: 36 ms, faster than 88.99% of Python online submissions for Balanced Binary Tree.
#Memory Usage: 17.9 MB, less than 48.53% of Python online submissions for Balanced Binary Tree.    

class Solution(object):
    def __init__(self):
        self.Balanced = True
        
    def find_height(self,root):
        
        if not root:
            return False
        
        left_height = self.find_height(root.left)
        right_height = self.find_height(root.right)
        # return if any sub-tree is unbalance
        if abs(left_height-right_height)>1:
            self.Balanced = False
            
        return 1+ max(left_height,right_height)
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
         _  = find_height(root)
        return self.Balanced