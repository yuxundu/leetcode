class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        visit = set()
        minHeap = [[0,k]]
        t = 0 
        while minHeap:
            w1,u1 = heapq.heappop(minHeap)
            if u1 in visit:
                continue
            visit.add(u1)
            t = w1
            for u2,w2 in adj[u1]:
                if u2 not in visit:
                    heapq.heappush(minHeap,[w1+w2,u2])

        return t if len(visit) == n else -1