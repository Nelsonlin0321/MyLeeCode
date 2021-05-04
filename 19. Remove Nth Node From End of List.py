#Runtime: 36 ms, faster than 46.86% of Python3 online submissions for Remove Nth Node From End of List.
#Memory Usage: 14.2 MB, less than 49.39% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#in one pass

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None
        
        i = 0
        n_prev_node_list = [] 
        n_node = head
        while (head is not None):
            
            if i>=n:
                n_prev_node_list.append(n_node)
                n_node = n_node.next
                
            head = head.next
            i+=1
            
        next_node =  n_node.next   
        if  len(n_prev_node_list)==0:
            return next_node
        connt_node = n_prev_node_list[-1]
        connt_node.next = next_node
        for i in range(len(n_prev_node_list)-2,-1,-1):
            prev_node=n_prev_node_list[i]
            prev_node.next = connt_node
            connt_node = prev_node
        return connt_node
                