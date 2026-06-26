class Twitter:

    def __init__(self):
        self.globalFeed = []
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.globalFeed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followSet = self.following[userId]
        followSet.add(userId)

        count = 0
        ret = []
        for i in range(len(self.globalFeed) - 1, -1, -1):
            user, tweet = self.globalFeed[i]

            if user in followSet:
                ret.append(tweet)
                count += 1
                if count == 10: break
        
        return ret
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
