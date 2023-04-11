class Solution:
    def alienOrder(self, words: List[str]) -> str:

        adj = {char : set() for word in words for char in word}

        for i in range(len(words)-1):
            first,second = words[i], words[i+1]
            minLen = min(len(first),len(second))
            if len(first) > len(second) and first[:minLen] == second[:minLen]:
                return ""
            for j in range(minLen):
                if first[j] != second[j]:
                    adj[first[j]].add(second[j])
                    break
        visiting = {}
        ans = []
        def dfs(c:str):
            if c in visiting:
                return visiting[c]
            visiting[c] = True

            for neighbour in adj[c]:
                if dfs(neighbour):
                    return True
            
            visiting[c] = False
            ans.append(c)
            return False
        
        for c in adj:
            if dfs(c):
                return ""

        ans.reverse()

        return "".join(ans)



