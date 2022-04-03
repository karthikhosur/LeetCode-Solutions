class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ''
        max_size = 0
        for i in s:
            if i not in temp :
                
                temp +=i
                
            else:
                temp = temp[temp.index(i)+1:]+i
                
            if max_size <=len(temp):
                max_size= len(temp)
                
        return max_size
    
  