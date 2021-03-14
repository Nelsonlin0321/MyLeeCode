# 03/14/2021 11:23  Accepted    144 ms  14.9 MB python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        greedy_index = 0
        assign_index= 0
        content_size = 0
        while((assign_index<=len(s)-1) and (greedy_index<=len(g)-1)):
            if s[assign_index]>=g[greedy_index]:
                greedy_index+=1
                content_size+=1
            assign_index+=1
        return content_size

#03/14/2021 11:05   Accepted    1408 ms 15 MB   python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        content_size = 0
        content_child_index=0
        for cookie_size in s:
            for child_greedy in g[content_child_index:]:
                if cookie_size >=child_greedy:
                    content_size +=1
                    content_child_index+=1
                    break
        return content_size