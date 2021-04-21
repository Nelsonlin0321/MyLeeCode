#https://leetcode.com/problems/implement-queue-using-stacks/submissions/
#Runtime: 16 ms, faster than 70.58% of Python online submissions for Implement Queue using Stacks.
#Memory Usage: 13.5 MB, less than 35.67% of Python online submissions for Implement Queue using Stacks.
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """  
        self.stack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack)!=0:
            num = self.stack[0]
            self.stack = self.stack[1:]
            return num
        else:
            return None
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        
        return self.stack[0] if len(self.stack)!=0 else None
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack)==0