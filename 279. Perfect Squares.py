#https://leetcode.com/problems/perfect-squares/submissions/
#Runtime: 5204 ms, faster than 18.06% of Python3 online submissions for Perfect Squares.
#Memory Usage: 14.3 MB, less than 74.78% of Python3 online submissions for Perfect Squares.
class Solution(object):
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo_list = [None for _ in range(n+1)]
        memo_list[0] = 0
        
        for i in range(1,n+1):
            print
            memo_list[i] = float("inf")
            
            j = 1
            while j*j <=i:
                memo_list[i] = min(memo_list[i],memo_list[i-j*j]+1)
                j+=1
        return memo_list[n]

#Runtime: 572 ms, faster than 74.19% of Python3 online submissions for Perfect Squares.
#Memory Usage: 35 MB, less than 9.34% of Python3 online submissions for Perfect Squares.
class Solution(object):
    
    def get_remain(self,n):

        j= int(math.sqrt(n)) # 获得能够平方的最大的数
        m_list = []
        while (0<j*j<=n):

            m = n-j*j
            m_list.append(m)

            j-=1
        return m_list
    
    def numSquares(self,n):
        if n ==0:
            return 0

        # 获取剩下的数
        queque = self.get_remain(n) # 初始化队列
        i = 1

        while len(queque)!=0:
            size = len(queque)
            for index in range(size): # 广度搜索 BFS
                num =queque[index]
                if num==0:
                    return i
                nums = self.get_remain(num)
                if 0 in nums: # 如果下一个队列有 0 的话, 说明不需要等待迭代到下一个队列，直接返回i+1
                    return i+1
                queque.extend(nums)
            queque = queque[size:]
            
            i+=1
            
