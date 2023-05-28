class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        dist = []
        for point in points:
            dist.append([pow(abs(point[0]),2)+pow(abs(point[1]),2),point[0],point[1]])
        heapq.heapify(dist)
        for i in range(k):
            d,x,y = heapq.heappop(dist)
            res.append([x,y])
        return res