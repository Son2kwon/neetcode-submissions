class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2); length = len(s1); s1 = sorted(s1)
        for i in range(0, n - length + 1):
            s = s2[i: i+length]
            s = sorted(s)

            if s == s1:
                return True

        return False


        

            

# Lowercase letters 만 들어오니까, counter 쓰기 좋네.
# 아, 이건 고정된 크기의 sliding window로 풀기 좋은데?
# 한 칸 씩 밀면서, s1이 있나 확인하는거지.
# sliding window의 특징은, 기존의 window의 정보를 재활용 한다니까...

# 좀 효율적으로 풀어보고 싶었는데 생각이 안 나니까 일단 풀어보자.
# 