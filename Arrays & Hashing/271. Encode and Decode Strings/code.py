class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ""
        for s in strs:
            ans = ans + str(len(s)) + "#" + s
        return ans
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans,index = [],0
        while index < len(s):
            limitation = s.index("#",index)
            index = limitation + 1 + int(s[index:limitation])
            ans.append(s[limitation+1:index])
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))