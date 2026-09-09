class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        count = Counter(hand)

        for v in sorted(count):
            if count[v] == 0: continue

            need = count[v]
            for i in range(v, v + groupSize):
                count[i] -= need
                if count[i] < 0: return False

        return True


# counter를 사용한 후에 sorted(c.items())
# 매번 가장 작은 값을 뽑아서 똑같은 방식으로 풀기