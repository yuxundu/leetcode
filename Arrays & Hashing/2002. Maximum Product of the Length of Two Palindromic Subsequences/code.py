class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palindromic = {}
        for mask in range(1,1<<n):
            subsequence = ""
            for j in range(n):
                if mask & (1<<j):
                    subsequence += s[j]
            if subsequence == subsequence[::-1]:
                palindromic[mask] = len(subsequence)
        res = 0;
        for m1 in palindromic:
            for m2 in palindromic:
                if m1 & m2 == 0:
                    res = max(res,palindromic[m1]*palindromic[m2])
        return res