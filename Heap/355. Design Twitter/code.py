class Twitter:

    def __init__(self):
        self.count = 0
        self.twittleMap = defaultdict(list)
        self.followMap = defaultdict(set)        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twittleMap[userId].append([self.count,tweetId])
        self.count -= 1     

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        minHeap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.twittleMap:
                index = len(self.twittleMap[followeeId]) - 1
                count, tweetId = self.twittleMap[followeeId][index]
                heapq.heappush(minHeap, [count,tweetId,followeeId,index-1])
            
        while minHeap and len(res) < 10:
            count,tweetId,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.twittleMap[followeeId][index]
                heapq.heappush(minHeap, [count,tweetId,followeeId,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)    


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)