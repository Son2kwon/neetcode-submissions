class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for index in range(0, 33):
            mask = 1 << index
            if (n & mask) != 0:
                count += 1
            
        return count

# 1의 개수라...
# 1로 가득 채운 것과 AND 연산하면 그대로 나올거고
# 0으로 가득 채운 것과 XOR 연산하면 그대로 나올거고
# 1로 가득 채운 것과 XOR 연산하면 0의 개수를 세면 되고

# 0001 하나씩 밀면서 AND 연산 결과가 0이냐 1이냐에 따라 세는 게 제일 간단하긴 하다
# 11 = 1101 and 