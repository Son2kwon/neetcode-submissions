class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        arr = [0 for _ in range(max(hand) + 1)] 

        for num in hand:
            arr[num] += 1

        while not all(x == 0 for x in arr):
            start = 0
            while arr[start] == 0:
                start += 1

            for i in range(start, start + groupSize):
                if i >= len(arr) or arr[i] == 0: return False
                arr[i] -= 1
            
        return True


# 음... 쭉 scan 하면서 hand에서 하나씩 빼는 게 제일 좋아보이는데 이건 BF니까.
# 일단 len(hand)가 groupSize의 배수가 아니라면 실패하겠는데?

# 힌트1: 여러 번 나올 수도 있는 minimum value는 group의 시작점이어야 함. Maybe a specific data structure can be useful
# 대놓고 Counter라고 주고 있는 것 같긴 한데... Counter 쓰면 편하긴 하겠다.
# Counter로 센 다음에, 가장 작은 value는 모든 group의 시작점으로 사용된다. 하나를 꺼내 groupSize 크기 만큼 다음 숫자들을 뺀다. 와중에 1 차이나는 친구가 없으면 False
# 가장 작은 value를 다 썼다면 다음으로 작은 value로 가서 똑같이 진행
# 근데 counter의 내용은 tuple이라 함부로 수정할 수 없구나.. 그렇다면..

# 힌트2: hash map을 사용 + sorting. Iterate through the sorted array and try to form groups by decrementing the frequency count.
# 그냥 내가 위에 생각한 거랑 똑같네. Counter 대신 그냥 hash 써야겠다.