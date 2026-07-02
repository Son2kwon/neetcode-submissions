class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = [0] * 26
        d = defaultdict(List[str])

        for s in strs:
            for c in s:
                counter[ord(c) - ord('a')] += 1

            k = tuple(counter)
            if k not in d:
                d[k] = list()
            d[k].append(s)

            counter = [0] * 26

        ans = []
        for v in d.values():
            ans.append(v)

        return ans

# dictionary의 key를 counter로, value를 List[str]으로 하면...
# 단, dictionary의 key는 변치않는 값이어야 하기 때문에 튜플을 key로 해야 함.

# Counter 끼리의 비교는 잘 하는데, tuple로 묶으니까 같아도 비교를 못 한다.
# 그냥 Counter를 쓰지 말고 26개 밖에 안 되는데, 그냥 자체적으로 counter를 만들까..?