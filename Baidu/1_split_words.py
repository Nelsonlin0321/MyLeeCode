#### 百度 NLP研发工程师面试题：根据词典进行分词
# 双指针
class Solution:
    def splitWords(self, word_dict,string):
        left = 0
        right = len(string)
        res = []
        while(left<right):
            sub_string = string[left:right]
            if sub_string in word_dict:
                left = right
                right = len(string)
                res.append(sub_string)
            elif len(sub_string)==1:
                left+=1
                right = len(string)
                res.append(sub_string)
            else:
                right-=1
        return res

word_dict = {'hello':3,'good':4,'say':8,'hey':1}

string = "youheymayhellogoodworld"

solution = Solution()

solution.splitWords(word_dict,string)