# Runtime: 24 ms, faster than 94.56% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.2 MB, less than 62.41% of Python3 online submissions for Letter Combinations of a Phone Number.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        int_char_dict = {'1':'',
                        '2':'abc',
                        '3':'def',
                        '4':'ghi',
                        '5':'jkl',
                        '6':'mno',
                        '7':'pqrs',
                        '8':'tuv',
                        '9':'wxyz'}
        char_list = []
        for char in digits:
            char_list.append(int_char_dict[char])
            
        comb_list  =[]
        for char in char_list[0]:
            comb_list.append([char])
        char_list =  char_list[1:]
        
        while (len(char_list)!=0):
            chars = char_list[0] #
            char_list = char_list[1:]

            size = len(comb_list)
            for index in range(size): 
                comb = comb_list[index] # [a]
                for char in chars: # d, e, f
                    new_comb = deepcopy(comb)
                    new_comb.append(char) #[a,d]
                    comb_list.append(new_comb)# [[a],[b],[c],[a,d]]

            # 把 [a],[b],[c] poll
            comb_list = comb_list[size:]
                # [[a,d],...]
                
        return [''.join(com) for com in comb_list]
    