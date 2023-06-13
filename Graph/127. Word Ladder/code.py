class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        if endWord not in wordList:
            return 0

        patterns = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        q = collections.deque()
        q.append(beginWord)
        visted = set()
        visted.add(beginWord)
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nextWord in patterns[pattern]:
                        if nextWord not in visted:
                            visted.add(nextWord)
                            q.append(nextWord)
            res += 1



        return 0