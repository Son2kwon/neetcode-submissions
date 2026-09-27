class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for num in counter.keys():
            if counter[num] == 1:
                return  num


# 시간 복잡도는 O(n), 공간 복잡도는 O(1)으로 유일하게 한 번 나오는 숫자를 찾아라

# Hash 쓰면 마음 편한데, 이걸 못 쓰게 하네...
# 