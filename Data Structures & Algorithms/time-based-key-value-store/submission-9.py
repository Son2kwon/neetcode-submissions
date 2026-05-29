class TimeMap:
    d = defaultdict(list)

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        aim = self.d[key]

        if len(aim) == 0:
            return ""
        
        if aim[0][0] > timestamp:
            return ""
        elif aim[-1][0] < timestamp:
            return aim[-1][1]

        left = 0; right = len(aim) - 1; ans = 0;
        print(aim)
        print(left, right, timestamp)

        while left <= right:
            mid = left + (right - left) // 2

            if aim[mid][0] == timestamp:
                ans = mid
                break
            elif aim[mid][0] < timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return aim[ans][1]

# 각 key 마다의 timestamp를 본다.