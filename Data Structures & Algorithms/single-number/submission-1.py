class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit = 0

        for num in nums:
            bit = bit ^ num

        return bit


# 시간 복잡도는 O(n), 공간 복잡도는 O(1)으로 유일하게 한 번 나오는 숫자를 찾아라

# Hash 쓰면 마음 편한데, 이걸 못 쓰게 하네...
# 추가 공간이 없어야 하니까 쓸 수 있는 건 변수

# 힌트 1: BF는 O(n^2). Data structure 중에 duplicate detect를 쉽게 해주는 애가 있을 것 같은데..
#   자료구조를 사용한다는 것 자체가 추가 공간이 있어야 된다는 건데?

# 힌트 2: Hash set을 그냥 사용하면 O(n) space. Bitwise Operator가 도움을 줄 수 있다.
#   XOR은 2번 하면 그대로 돌아온다. 이걸 사용하면
#   0000 0000 을 만들어 놓고, 들어온 숫자의 비트를 1로 만든 비트를 만들어 XOR.
#   마지막에 몇 번째 비트가 살아남아 있는지 확인하고, 그걸 return 하면 된다.