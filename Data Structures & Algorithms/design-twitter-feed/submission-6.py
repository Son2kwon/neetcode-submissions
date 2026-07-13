class Twitter:
    user_tweet: defaultdict
    user_follow: defaultdict
    time: int

    def __init__(self):
        self.user_tweet = defaultdict(list)
        self.user_follow = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for tweet in self.user_tweet[userId]:
            if len(heap) < 10:
                heapq.heappush(heap, tweet)
            else:
                heapq.heapreplace(heap, tweet)

        for user in self.user_follow[userId]:
            if user == userId:
                continue

            for tweet in self.user_tweet[user]:
                if len(heap) < 10:
                    heapq.heappush(heap, tweet)
                else:
                    heapq.heapreplace(heap, tweet)

        ans = []
        heap = sorted(heap)

        for time, tweet in heap:
            ans.append(tweet)

        return list(reversed(ans))


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follow[followerId]:
            return
        self.user_follow[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.user_follow[followerId]:
            return
        self.user_follow[followerId].remove(followeeId)
        
# 하다하다 트위터를 만들라고 하네. 일론 머스크가 트위터 코드를 깠다고는 하지만...

# 10 most recent tweets 니까 이것도 힙을 사용하나..?
# A가 B를 follow 했다고 B가 A를 follow 한 것은 아님...

# dict를 사용해서 {userId: tweetId}로 관리하고
# dict를 사용해서 {userId: followeeId}도 관리 -> followeeId에는 자기자신을 항상 포함
# postTweet은 tweetId에 append
# follow는 followeeId에 append, unfollow는 followeeId에서 삭제
# getNewsFeed는 tweetId가 늘 오름차순이면 그냥 하면 되는데... 늘 오름차순이라는 조건은 없으니까
#   그럼 오름차순인 무언가를 내가 넣어놓으면 되나? -> (time, tweetId) 한 쌍으로 저장해야겠다.
#   크기가 10인 최소힙을 만들어서 update, time이 큰 순서대로 반환하면 된다.