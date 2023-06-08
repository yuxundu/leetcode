class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitMap ={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def dfs(i, currStr):
            if i >= len(digits):
                res.append(currStr)
                return
            for j in digitMap[digits[i]]:
                dfs(i+1, currStr + j)
        if digits:
            dfs(0,"")
        return res