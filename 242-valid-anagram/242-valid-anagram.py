class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a=[0]*26 
        for i in range(len(s)):
            a[ord(s[i])-97]+=1
            a[ord(t[i])-97]-=1
        return a==[0]*26
        