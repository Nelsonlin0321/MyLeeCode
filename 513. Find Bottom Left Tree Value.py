#https://leetcode.com/problems/find-bottom-left-tree-value/submissions/
# Runtime: 28 ms, faster than 96.20% of Python online submissions for Find Bottom Left Tree Value.
# Memory Usage: 18.4 MB, less than 18.25% of Python online submissions for Find Bottom Left Tree Value.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS
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
                
#Runtime: 28 ms, faster than 99.67% of Python3 online submissions for Find Bottom Left Tree Value.
#Memory Usage: 16.5 MB, less than 53.09% of Python3 online submissions for Find Bottom Left Tree Value.
#BFS
class Solution(object):
    def __init__(self):
        self.value_list = []
        
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        """
        if root is None:
            return None
        
        queque = [[root]]
#         value_list = []
        # # 当queque 等 0 的时候，已经遍历完最后一个node， 此时的curr_queque 存着就是最后一个层级
        #所以这次第一个元素就是 Left Bottom
        while (len(queque)!=0): 
            #  获取當前层级所有顶点
            curr_queque = queque[0]
            queque = queque[1:] 
            next_queque = [] #用与储存这个层级的点用作下一个循环遍历
            for node in curr_queque:
                if node.left is not None:
                    next_queque.append(node.left)
                if node.right is not None:
                    next_queque.append(node.right)
            if len(next_queque)!=0:
                queque.append(next_queque)
        
        return curr_queque[0].val
  
                    
                    
            
        
            
        
            
        