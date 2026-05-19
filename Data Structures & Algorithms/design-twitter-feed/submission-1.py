class Twitter:

    def __init__(self):
        # we wanna map users to followed
        # keep list of tweets with user, newest first, filter 
        # filter constant time with set of followed
        self.tweets = []
        self.follows = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        # O(1)
        self.tweets.append((userId, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        # O(nb of tweets) -> that's pretty bad
        # we may wanna rather have a precomputer list per user
        # this is porbbaly the most common action
        # best case O(10)
        found = []
        i = len(self.tweets)-1
        while i >= 0 and len(found) < 10:
            u, t = self.tweets[i]
            if u == userId or u in self.follows[userId]:
                found.append(t)
            i -= 1
        return found

    def follow(self, followerId: int, followeeId: int) -> None:
        # O(1)
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # O(followed)
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
