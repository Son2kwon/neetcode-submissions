class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i in range(3):
            for idx, triplet in enumerate(triplets):
                print(idx, triplet)
                if target[i] < triplet[i]:
                    triplets.pop(idx)

        ans = [0, 0, 0]
        for triplet in triplets:
            ans = [max(ans[0], triplet[0]), max(ans[1], triplet[1]), max(ans[2], triplet[2])]

        print(ans)

        return ans == target

# 그냥 i번째 원소들의 최대값들의 list == target 이렇게 보면 되는 거 아닌가?
# 딱히 실행 순서에 따라 뭐 불이익 받는 것도 아닌 것 같은데

# 아 triplets 들의 조합으로 target을 만들 수 있냐구나. 그러면 무조건 막 전체를 다 안 써도 되겠네?

# 음.. target[0]를 찾아보고, 그 숫자 포함하는 triplet 있으면 그거 가져오고, 없으면 return False
# target[1]도 마찬가지로 진행
# target[2]도 마찬가지로 진행
# 그렇게 만들어진 triplet이 target과 같으면 true, 아니면 false

# 너무 단순하게 푸니까 edge case를 너무 빨리 만난다.
# 음... 아니면 애들을 빼는 식으로 가볼까?
# triplet 중에서 첫번째 숫자가 target[0] 이하인 애들만 남겨두고
# 남은 애들 중에서 두번째, 또 남은 애들 중에서 세번째 애들도 남겨둔 다음에
# triplet 만들어서 target이랑 비교

"""
[2,4,4],[2,6,1],[10,9,4],[10,4,1],[1,4,2],[6,2,9]
"""