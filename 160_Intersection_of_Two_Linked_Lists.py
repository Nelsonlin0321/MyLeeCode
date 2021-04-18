# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 176 ms, faster than 98.08% of Python online submissions for Intersection of Two Linked Lists.
# Memory Usage: 43.4 MB, less than 34.17% of Python online submissions for Intersection of Two Linked Lists.

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            A, B = headA, headB
            while A!=B:
                # print(A)
                # print(B) # None
                # print("="*10)
                A = A.next if A else headB
                B = B.next if B else headA
            return A