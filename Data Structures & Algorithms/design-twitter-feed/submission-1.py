class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = collections.defaultdict(list)
        self.follows = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        data = self.tweets[userId][:]
        for fu in self.follows[userId]:
            data += self.tweets[fu]
        heapq.heapify(data)
        ret = []
        while data and len(ret)<10:
            _, ti = heapq.heappop(data)
            ret.append(ti)
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)