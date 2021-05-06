#Runtime: 36 ms, faster than 53.84% of Python3 online submissions for Binary Tree Level Order Traversal.
#Memory Usage: 14.4 MB, less than 96.76% of Python3 online submissions for Binary Tree Level Order Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
        
        queque  = [[root]] # 记录需要向下横向遍历的点
        order_list = [[root.val]]
        while (len(queque)!=0):
            node_list = []
            next_queque = []
            # 获取当前层
            curr_queque = queque[0]
            queque = queque[1:] # 这一层从队列中pop 出
            for root_node in curr_queque: # 每一层的所有node
                # 把 这层的 left right  加进行
                left_node = root_node.left
                
                if left_node is not None:
                    node_list.append(left_node.val)
                    next_queque.append(left_node)
                    
                right_node = root_node.right 
                if right_node is not None:
                    node_list.append(right_node.val)
                    next_queque.append(right_node)
                
            if len(next_queque)!=0:
                #  这一层遍历完毕后，添加下一层 
                queque.append(next_queque)
                order_list.append(node_list)
        
        return order_list