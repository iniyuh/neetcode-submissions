class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (self.time, userId, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followSet = self.following[userId]
        followSet.add(userId)

        workingHeap = []
        for followeeId in followSet:
            if self.tweets[followeeId]:
                heapq.heappush(workingHeap, self.tweets[followeeId][0])
        
        i = 0
        removedList = []
        ret = []
        while i < 10 and workingHeap:
            _, followeeId, tweetId = heapq.heappop(workingHeap)

            ret.append(tweetId)
            i += 1

            removedList.append(heapq.heappop(self.tweets[followeeId]))
            if self.tweets[followeeId]:
                heapq.heappush(workingHeap, self.tweets[followeeId][0])
        
        for value in removedList:
            heapq.heappush(self.tweets[value[1]], value)


        return ret
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
