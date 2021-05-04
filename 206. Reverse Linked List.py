#Runtime: 32 ms, faster than 85.40% of Python3 online submissions for Reverse Linked List.
#Memory Usage: 15.5 MB, less than 92.66% of Python3 online submissions for Reverse Linked List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev_node = None
        
        if head is None:
            return None
        
        while ((head is not None)):
            
            curr_node = head # 获取当前节点
            
            next_node = head.next # 保存当前节点的下一个节点
            
            curr_node.next = prev_node # 将指针指向上一个节点
            
            prev_node = curr_node # 当前节点作为下一个节点的上一个节点
            
            head = next_node
        
        return curr_node
            
            
        
