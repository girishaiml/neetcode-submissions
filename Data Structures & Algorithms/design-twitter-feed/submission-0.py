from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # User sees their own tweets + tweets from people they follow
        users = self.following[userId] | {userId}

        # Add each user's most recent tweet
        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        # Get at most 10 most recent tweets
        while heap and len(res) < 10:
            negTime, tweetId, user, index = heapq.heappop(heap)

            res.append(tweetId)

            # Add this user's next-most-recent tweet
            if index > 0:
                index -= 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
