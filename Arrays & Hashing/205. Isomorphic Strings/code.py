class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        for i in  range(len(s)):
            if s[i] in sMap and sMap[s[i]]!= t[i]:
                return False
            if t[i] in tMap and s[i]!= tMap[t[i]]:
                return False
            if s[i] not in sMap:
                sMap[s[i]] = t[i]
            if t[i] not in tMap:
                tMap[t[i]] = s[i]
        
        return True