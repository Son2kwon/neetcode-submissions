class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            ans.append(i.bit_count())

        return ans


# n이 주어지면 0부터 n까지의 수들의 1의 개수를 출력하라

# 2^k (k >= 0 정수)일 때 1
# 2^k ~ 2^(k+1) - 1 까지 1씩 증가
# 생각해보니 이것도 아니네..