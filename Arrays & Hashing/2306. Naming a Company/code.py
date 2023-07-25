class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        firstLetterGroup = collections.defaultdict(set)
        for name in ideas:
            firstLetterGroup[name[0]].add(name[1:])
        res = 0 
        for c1 in firstLetterGroup:
            for c2 in firstLetterGroup:
                if c1 == c2:
                    continue
                intersect = 0
                for a in firstLetterGroup[c1]:
                    if a in firstLetterGroup[c2]:
                        intersect += 1
                res += (len(firstLetterGroup[c1])-intersect) * (len(firstLetterGroup[c2])-intersect)
     

        return res