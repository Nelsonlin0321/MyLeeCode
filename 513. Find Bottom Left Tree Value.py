#https://leetcode.com/problems/find-bottom-left-tree-value/submissions/
#Runtime: 36 ms, faster than 55.89% of Python online submissions for Find Bottom Left Tree Value.
#Memory Usage: 18.3 MB, less than 24.71% of Python online submissions for Find Bottom Left Tree Value.
class Solution(object):
    def __init__(self):
        self.value_list = []
        
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## left = 1
        ## right = 0
        self.find_deepest_left(root,0,1)
        
        max_deepth = max([ deepth for (deepth,pos,value) in self.value_list])
        max_left_pos = max( [ pos for (deepth,pos,value) in self.value_list if deepth ==max_deepth])
        return [ value for (deepth,pos,value) in self.value_list if deepth ==max_deepth and pos==max_left_pos][0]
        
    def find_deepest_left(self,root,deepth,left_or_right):
        if (root.left is None and root.right is None ):
            self.value_list.append((deepth,left_or_right,root.val)) 
        else:
            if root.left is not None:
                left_deepth = deepth+1
                self.find_deepest_left(root.left,left_deepth,1)
            if root.right is not None:
                right_deepth = deepth+1
                self.find_deepest_left(root.right,right_deepth,0)
            
        