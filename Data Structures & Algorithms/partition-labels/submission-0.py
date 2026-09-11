class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = dict()
        ans = []; size = 0; end = 0;

        for i, c in enumerate(s):
            last[c] = i

        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                ans.append(size + 1)
                size = 0
            else:
                size += 1

        return ans


# 각 문자가 한 substring에만 나타나도록 하면서 최대한 많이 나눠라
# 겹치는 애들은 최대한 하나로 묶고
# 겹치는 애들 없으면 싹 다 나누고

# x -> x, y -> xyx -> xyxx -> xyxxy -> xyxxy, z -> xyxxy, z, b -> xyxxy, zbz ...
# 이런 느낌으로다가 하는 것 같은디

# x -> 0, y -> 0

# 힌트1: character는 first and last index가 있다. 이걸로 greedy를 할 수 있을까?
# character가 겹치게 된다면 그 사이를 전부 substring으로 묶는다.

# 힌트2: 각 character들의 last index를 저장해둔다. 반복문을 돌리면서 각 Index를 potential start of a partition으로 가정 후 최대한 멀리 본다. size라는 변수로 current partition을 저장해둔다.

# 힌트3: 현재 partition의 end를 maximum last index of the charaters를 기준으로 update. current index == last index 라면 partition 끝