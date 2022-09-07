class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_indx={}
        max_length=0
        start_index=0
        
        for i in range(len(s)):
            if s[i] in last_indx:
                start_index=max(start_index,last_indx[s[i]]+1)
            max_length=max(max_length,i-start_index+1)
            last_indx[s[i]]=i
        return max_length