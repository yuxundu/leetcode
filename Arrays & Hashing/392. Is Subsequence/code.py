class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0

        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return True if i == len(s) else False
        

        
