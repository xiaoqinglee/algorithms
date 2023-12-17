from collections import deque, defaultdict
from collections.abc import Iterable, Iterator
from itertools import count, islice
import heapq


# https://leetcode.cn/problems/design-twitter
class Twitter:

    def __init__(self):
        self.desc_timestamp_gen: Iterator[int] = count(start=0, step=-1)
        # deque 元素: tuple[tweet_timestamp, tweet_id]
        self.user_to_tweets: defaultdict[int, deque[tuple[int, int]]] = defaultdict(deque)
        # fan_to_stars
        self.user_to_followee: defaultdict[int, set[int]] = defaultdict(set)

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.user_to_tweets[user_id].appendleft((next(self.desc_timestamp_gen), tweet_id))

    def getNewsFeed(self, user_id: int) -> list[int]:
        tweets_gen: Iterable[int] = heapq.merge(
            *(self.user_to_tweets[u] for u in (self.user_to_followee[user_id] | {user_id})))
        return [tweet for tweet_timestamp, tweet in islice(tweets_gen, 10)]

    def follow(self, follower_id: int, followee_id: int) -> None:
        if followee_id == follower_id:
            return
        self.user_to_followee[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id not in self.user_to_followee[follower_id]:
            return
        self.user_to_followee[follower_id].remove(followee_id)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
