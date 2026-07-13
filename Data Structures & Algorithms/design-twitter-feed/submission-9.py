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
        # 각 유저의 가장 최신 트윗을 최대힙에 넣음 (time * -1, tweetId, userId, index)
        ans = []
        heap = []
        if len(self.user_tweet[userId]) > 0:
            heapq.heappush(heap, (self.user_tweet[userId][-1][0] * -1, self.user_tweet[userId][-1][1], userId, len(self.user_tweet[userId]) - 1))
        for user in self.user_follow[userId]:
            if userId == user:
                continue
            heapq.heappush(heap, (self.user_tweet[user][-1][0] * -1, self.user_tweet[user][-1][1], user, len(self.user_tweet[user]) - 1))

        # 10번 반복
        for i in range(0, 10):
            # 트윗이 10개 보다 작을 때
            if len(heap) == 0:
                break
            # heap에서 pop
            cur = heapq.heappop(heap)
            # pop된 유저의 다음 트윗을 heap에 넣음
            cur_tweet = cur[1]; cur_user = cur[2]; cur_index = cur[3];
            ans.append(cur_tweet)
            # 현재 user의 tweet이 남아있다면 heappush, 아니라면 끝
            if cur_index > 0:
                heapq.heappush(heap, (self.user_tweet[cur_user][cur_index - 1][0] * -1, self.user_tweet[cur_user][cur_index - 1][1], cur_user, cur_index - 1))

        return ans

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
# dict를 사용해서 {userId: followeeId}도 관리
# postTweet은 tweetId에 append
# follow는 followeeId에 append, unfollow는 followeeId에서 삭제
# getNewsFeed는 tweetId가 늘 오름차순이면 그냥 하면 되는데... 늘 오름차순이라는 조건은 없으니까
#   그럼 오름차순인 무언가를 내가 넣어놓으면 되나? -> (time, tweetId) 한 쌍으로 저장해야겠다.
#   크기가 10인 최소힙을 만들어서 update, time이 큰 순서대로 반환하면 된다.

# 덕분에 복잡도가 미쳐 날뛰는 것 같긴 한데..

# Time Complexity: O(m * n): m은 팔로잉 하는 사람 수, n은 tweet 개수
# Space Complexity: O(m + n)