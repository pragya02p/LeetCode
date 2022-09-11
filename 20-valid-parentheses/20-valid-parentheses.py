class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(' or i=='['or i=='{':
                l.append(i)
            else:
                if l==[]:
                    return False
                c=l.pop()
                if c=='(' and i!=')':
                    return False
                elif c=='[' and i!=']':
                    return False
                elif c=='{' and i!='}':
                    return False
            
    
        if l==[]:
            return True
        else:
            return False
        
        