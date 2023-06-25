class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i,v in enumerate(s):
            lastIndex[v] = i

        res = []
        size = 0
        end = 0
        for i,v in enumerate(s):
            size += 1
            end = max(end,lastIndex[v])
            if end == len(s)-1:
                size += end -i
                res.append(size)
                break
            if i == end:
                res.append(size)
                size = 0

        return res